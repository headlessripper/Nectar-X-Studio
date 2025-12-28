from PyQt6.QtWidgets import QLineEdit, QCompleter
from PyQt6.QtCore import Qt, QTimer, QStringListModel, QRunnable, QThreadPool
import requests
from scripts.SYS_Config.Config import DEFAULT_SUGGESTIONS, MAX_HISTORY
from scripts.components.Service.find_icon import find_icon
from scripts.components.WidgetBased.Notify import Notify
from winotify import Notification, audio

class RunnableTask(QRunnable):
    def __init__(self, fn, *args):
        super().__init__()
        self.fn = fn
        self.args = args

    def run(self):
        self.fn(*self.args)

class SearchLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Search")
        self.setFixedHeight(36)
        self.setStyleSheet(
            "background: rgba(255,255,255,0.02); padding-left:12px; border-radius:10px; color:#bdbdbd;"
        )
    
        self.search_history = []
        self.typing_timer = QTimer()
        self.typing_timer.setSingleShot(True)
        self.typing_timer.setInterval(300)
        self.typing_timer.timeout.connect(self.fetch_web_suggestions)

        self.completer_model = QStringListModel()
        self.completer = QCompleter(self.completer_model, self)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.setCompleter(self.completer)

        self.threadpool = QThreadPool.globalInstance()

        self.textChanged.connect(self.on_text_changed)
        self.returnPressed.connect(self.run_search_thread)

    def on_text_changed(self, text):
        if text.strip():
            self.typing_timer.start()

    def fetch_web_suggestions(self):
        self.typing_timer.stop()
        query = self.text().strip()
        if not query:
            return
        self.threadpool.start(RunnableTask(self._fetch_suggestions_threaded, query))

    def _fetch_suggestions_threaded(self, query):
        try:
            response = requests.get(
                'https://suggestqueries.google.com/complete/search',
                params={'client': 'firefox', 'q': query},
                timeout=2
            )
            suggestions = response.json()[1]
        except Exception as e:
            toast = Notification(
                app_id="Nectar-X-Studio",
                title="Web suggestion Error",
                msg=f"Web suggestion Error: No Internet or {e}",
                icon=find_icon('background/NectarX.png'),
                duration="short"
            )
            toast.set_audio(audio.SMS, loop=False)
            toast.show()
            suggestions = []

        # Merge web suggestions, history, and defaults
        combined = list(dict.fromkeys(suggestions + self.search_history + DEFAULT_SUGGESTIONS))
        self.completer_model.setStringList(combined)

    def run_search_thread(self):
        url_str = self.text().strip()
        if not url_str:
            return
        if url_str not in self.search_history:
            self.search_history.insert(0, url_str)
            self.search_history = self.search_history[:MAX_HISTORY]

        Notify("Coming Soon!", parent=self)