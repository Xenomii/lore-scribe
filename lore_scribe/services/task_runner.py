from PySide6.QtCore import QObject, QRunnable, Signal, Slot, QThreadPool

class TaskSignal(QObject):
    """
    Custom signal class to handle task completion and errors.
    """
    task_completed = Signal(object)
    task_error = Signal(Exception)

class BackgroundTask(QRunnable):
    """
    A background task that can be run in a separate thread.
    """
    def __init__(self, task_function, *args, **kwargs):
        super().__init__()
        self.task_function = task_function
        self.args = args
        self.kwargs = kwargs
        self.signals = TaskSignal()

    @Slot()
    def run(self):
        """
        Run the task and emit signals on completion or error.
        """
        print(f"[TaskRunner] Running task: {self.task_function.__name__} with args: {self.args} and kwargs: {self.kwargs}")
        try:
            result = self.task_function(*self.args, **self.kwargs)
            self.signals.task_completed.emit(result)
        except Exception as e:
            self.signals.task_error.emit(e)

class TaskRunner:
    """
    A service to run tasks in the background using a thread pool.
    """
    def __init__(self):
        self.thread_pool = QThreadPool().globalInstance()

    def run_task(self, task_function, *args, on_result=None, on_error=None, **kwargs):
        """
        Run a task in the background.

        Args:
            task_function (callable): The function to run as a task.
            *args: Positional arguments for the task function.
            **kwargs: Keyword arguments for the task function.
        """
        background_task = BackgroundTask(task_function, *args, **kwargs)

        if on_result:
            background_task.signals.task_completed.connect(on_result)
        if on_error:
            background_task.signals.task_error.connect(on_error)
        
        self.thread_pool.start(background_task)
        return background_task.signals