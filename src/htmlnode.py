class HTMLnode:
    def __init__(self, tag = None, value = None, children = None, props = None):        
        pass

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        
