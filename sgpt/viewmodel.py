import dummymodel
import qtview
import threading

class ViewModel:
    def __init__(self, model, view, argv):
        self.model = model()
        self.view = view()
        self.chatlist = []
        self.last_question = ""
        self.erased = False

        self.view.enterhook.append(self.enterfunc)
        self.view.reverthook.append(self.revertfunc)
        self.view.retryhook.append(self.retryfunc)

        self.threadevent = threading.Event()
        self.thread = threading.Thread(target=self.mainloop)
        self.thread.start()

        self.view.exec()

    def mainloop(self):
        while True:
            if self.threadevent.is_set():
                self.threadevent.clear()
                self.chatlist.append(self.last_question)
                self.update_log()
                self.chatlist.append(self.model.enter_prompt(self.last_question))
                self.update_log()
        
    def enterfunc(self, text):
        print(text)
        self.last_question = text
        self.erased = False
        self.threadevent.set()

    def update_log(self):
        self.view.set_text('\n'.join(self.chatlist))

    def revertfunc(self):
        print("revert")
        if len(self.chatlist) < 2:
            return
        del self.chatlist[-1]
        del self.chatlist[-1]
        self.update_log()
        self.erased = True

    def retryfunc(self):
        print("retry")
        if not self.erased:
            self.revertfunc()
        self.threadevent.set()
        self.update_log()
        self.erased = False

    def getoutputfunc(self):
        print("register")

def exec(argv):
    qtview.init(argv)
    vm = ViewModel(dummymodel.Dummymodel, qtview.View, argv)
