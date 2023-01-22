import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QColor, QGuiApplication, QFontDatabase, QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QVBoxLayout, QWidget, QDesktopWidget

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")  #Title
        self.setGeometry(100, 100, 800, 600) #screen opening width-height

        # this line of code is added to change the background color to grey
        custom_color = QColor(224, 224, 224) # set the R, G, B values of the color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), custom_color)
        self.setPalette(palette)

        # Create the search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search Google or type URL")
        self.search_bar.setFixedWidth(575)
        self.search_bar.setFixedHeight(30)
        self.search_bar.setStyleSheet("""
        margin: 0px 3px; 
        height: 35px; 
        width: 120px; 
        border-radius: 6px;
        color: #5c5c5c; 
        background-color: #f2f2f; 
        font-weight: normal; 
        font-size: 14px;
        box-shadow: 2px 2px 5px #000000;
        """)
        self.search_bar.setAlignment(Qt.AlignCenter)


        # Load the font file into the application
        font_id = QFontDatabase.addApplicationFont(r"C:\Users\Zayn\Downloads\sf-pro-display-cufonfonts\SFPRODISPLAYREGULAR.OTF")

        font_name = QFontDatabase.applicationFontFamilies(font_id)[0] # Get the font family name from the font file
        font = QFont(font_name) # Create a font object using the font family name
        self.search_bar.setFont(font)         # Set the font of the search bar to Quicksand

        # Create the web view
        self.web_view = QWebEngineView(self)

        # Create the layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.search_bar,0,Qt.AlignHCenter)
        layout.addWidget(self.web_view)
        layout.setContentsMargins(0, 9, 0, 0)   #To set margins (to make the white area below the search bar as wide as the application width)
        
        # Connect the search bar to the web view
        self.search_bar.returnPressed.connect(self.load_url)

    def load_url(self):
        url = self.search_bar.text()
        if not url.startswith("http"):
            url = "https://www.google.com/search?q=" + url
        self.web_view.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
