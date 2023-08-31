import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QListWidget, QTextEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QAction, QMenu, QLineEdit, QFileDialog

class NotesApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.notes_directory = "notes"
        if not os.path.exists(self.notes_directory):
            os.makedirs(self.notes_directory)

        self.init_ui()

    def init_ui(self):
        self.menu_bar = self.menuBar()  # Create the menu bar
        self.setMenuBar(self.menu_bar)  # Add the menu bar to the main window
    
        # Add menus and actions to the menu bar
        file_menu = self.menu_bar.addMenu("File")
        edit_menu = self.menu_bar.addMenu("Edit")
        self.setWindowTitle("PyPad")
        self.setGeometry(100, 100, 800, 600)

        

        self.sidebar = QListWidget()
        self.load_notes()  # Load notes on app startup
        self.sidebar.itemClicked.connect(self.load_note)

        self.editor = QTextEdit()

        self.splitter = QSplitter(self)
        self.splitter.setOrientation(0x1)  # Vertical orientation
        self.splitter.addWidget(self.sidebar)
        self.splitter.addWidget(self.editor)

        self.sidebar.setMinimumWidth(150)  # Adjust sidebar width
        self.sidebar.setMaximumWidth(150)

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_note)
        self.save_button.setMaximumWidth(60)  # Adjust button size

        self.new_note_button = QPushButton("+", self)
        self.new_note_button.clicked.connect(self.create_new_note)
        self.new_note_button.setMaximumWidth(40)  # Adjust button size

        self.rename_button = QPushButton("Rename", self)
        self.rename_button.clicked.connect(self.rename_note)
        self.rename_button.setMaximumWidth(70)  # Adjust button size

        self.delete_button = QPushButton("Delete Note", self)
        self.delete_button.clicked.connect(self.delete_note)
        self.delete_button.setMaximumWidth(90)  # Adjust button size

        self.change_dir_button = QPushButton("Notebooks", self)
        self.change_dir_button.clicked.connect(self.change_directory)
        self.change_dir_button.setMaximumWidth(130)  # Adjust button size

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.save_button)
        buttons_layout.addWidget(self.new_note_button)
        buttons_layout.addWidget(self.rename_button)
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addWidget(self.change_dir_button)
        buttons_layout.addStretch()  # Push buttons to the left

        main_layout = QVBoxLayout()
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.splitter)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def load_notes(self):
        notes = os.listdir(self.notes_directory)
        self.sidebar.clear()
        self.sidebar.addItems([note[:-4] for note in notes if note.endswith('.txt')])

    def load_note(self, item):
        note_name = item.text() + ".txt"
        note_path = os.path.join(self.notes_directory, note_name)
        with open(note_path, "r") as f:
            lines = f.readlines()
            title = lines[0].strip()
            content = "\n".join(lines[1:])
            self.editor.setPlainText(content)
            self.editor.setWindowTitle(title)

    def save_note(self):
        note_content = self.editor.toPlainText()
        note_title = self.editor.windowTitle()
        selected_item = self.sidebar.currentItem()
        if selected_item:
            note_name = selected_item.text() + ".txt"
            note_path = os.path.join(self.notes_directory, note_name)
            with open(note_path, "w") as f:
                f.write(note_title + "\n" + note_content)
            self.load_notes()  # Update the sidebar with the saved note

    def create_new_note(self):
        new_note_name = "New Note.txt"
        new_note_path = os.path.join(self.notes_directory, new_note_name)
        with open(new_note_path, "w") as f:
            f.write("New Note\n")  # Default title
        self.load_notes()  # Update the sidebar with the new note

    def rename_note(self):
        selected_item = self.sidebar.currentItem()
        if selected_item:
            note_name = selected_item.text()
            self.rename_edit = QLineEdit(note_name, self.sidebar)
            self.rename_edit.editingFinished.connect(self.rename_note_accept)
            self.sidebar.setItemWidget(selected_item, self.rename_edit)
            self.rename_edit.selectAll()
            self.rename_edit.setFocus()

    def rename_note_accept(self):
        selected_item = self.sidebar.currentItem()
        new_note_name = self.rename_edit.text()
        if selected_item and new_note_name:
            old_note_name = selected_item.text()
            old_note_path = os.path.join(self.notes_directory, old_note_name + ".txt")
            new_note_path = os.path.join(self.notes_directory, new_note_name + ".txt")
            os.rename(old_note_path, new_note_path)
            self.load_notes()  # Update the sidebar with the renamed note

    def delete_note(self):
        selected_item = self.sidebar.currentItem()
        if selected_item:
            note_name = selected_item.text() + ".txt"
            note_path = os.path.join(self.notes_directory, note_name)
            os.remove(note_path)
            self.load_notes()  # Update the sidebar after deleting the note

    def change_directory(self):
        new_directory = QFileDialog.getExistingDirectory(self, "Select Notebook Directory")
        if new_directory:
            self.notes_directory = new_directory
            relative_path = os.path.relpath(self.notes_directory, start=self.notes_directory)
            self.setWindowTitle(f"Notes App - {relative_path}")
            print(relative_path)
            self.load_notes()  # Update the sidebar with notes from the new directory

if __name__ == "__main__":
    app = QApplication(sys.argv)
    notes_app = NotesApp()
    notes_app.show()
    sys.exit(app.exec_())
