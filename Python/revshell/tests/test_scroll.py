

The easiest way would be to use a QTextEdit, probably set it to read only through setReadOnly() and append your text with the append() or insertPlainText() method. I roughly used something like the following for a similar use case:

Basic Snippet:

...
logOutput = QTextEdit(parent)
logOutput.setReadOnly(True)
logOutput.setLineWrapMode(QTextEdit.NoWrap)

font = logOutput.font()
font.setFamily("Courier")
font.setPointSize(10)

theLayout.addWidget(logOutput)
...

To append text in an arbitrary color to the end of the text area and to automatically scroll the text area so that the new text is always visible, you can use something like

Automatic Scroll Snippet:

...
logOutput.moveCursor(QTextCursor.End)
logOutput.setCurrentFont(font)
logOutput.setTextColor(color)

logOutput.insertPlainText(text)

sb = logOutput.verticalScrollBar()
sb.setValue(sb.maximum())
...
