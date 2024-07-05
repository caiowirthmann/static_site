class HTMLnode:
    def __init__(self, tag = None, value = None, children = None, props = None):        
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props #    props is a dict{} with attributes of html tag

    def to_html(self):
        raise NotImplementedError ("to html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
          props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLnode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value is None:
            raise ValueError ("leaf nodes require a value to render as a HTML")
        
        if self.tag is None:
            return f"{self.value}"
        
        #starts constructing the HTML string <....
        html_string = f"<{self.tag}"

        if self.props:
            for key, val in self.props.items():
                # add HTML tag and corresponding value. example--> "href" tag and link
                html_string += f' {key}="{val}"'
        #close first tag <.., and value from node and close tag with </tag>
        html_string += f'>{self.value}</{self.tag}>'

        return html_string