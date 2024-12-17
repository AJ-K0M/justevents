from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from database import init_db, add_user, add_vendor, get_vendors, add_event, get_events

# Home Screen
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=20)
        layout.add_widget(MDLabel(text="ASA EVENTS", halign="center", font_style="H4"))

        layout.add_widget(MDRaisedButton(text="Sign Up as Client", on_press=lambda x: self.manager.current = "register"))
        layout.add_widget(MDRaisedButton(text="Sign Up as Vendor", on_press=lambda x: self.manager.current = "vendor"))
        layout.add_widget(MDRaisedButton(text="Client Dashboard", on_press=lambda x: self.manager.current = "client_dashboard"))

        self.add_widget(layout)

# User Registration Screen
class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=10)
        layout.add_widget(MDLabel(text="Client Registration", halign="center", font_style="H5"))

        self.username = MDTextField(hint_text="Username")
        self.password = MDTextField(hint_text="Password", password=True)
        self.email = MDTextField(hint_text="Email")

        submit_btn = MDRaisedButton(text="Register", on_press=self.register_user)

        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.email)
        layout.add_widget(submit_btn)
        layout.add_widget(MDRaisedButton(text="Back", on_press=lambda x: self.manager.current = "home"))

        self.add_widget(layout)

    def register_user(self, instance):
        add_user(self.username.text, self.password.text, "client", self.email.text)
        print("Client Registered Successfully!")
        self.manager.current = "home"

# Vendor Registration Screen
class VendorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=10)
        layout.add_widget(MDLabel(text="Vendor Registration", halign="center", font_style="H5"))

        self.name = MDTextField(hint_text="Vendor Name")
        self.service_type = MDTextField(hint_text="Service Type")
        self.location = MDTextField(hint_text="Location")

        submit_btn = MDRaisedButton(text="Register", on_press=self.register_vendor)

        layout.add_widget(self.name)
        layout.add_widget(self.service_type)
        layout.add_widget(self.location)
        layout.add_widget(submit_btn)
        layout.add_widget(MDRaisedButton(text="Back", on_press=lambda x: self.manager.current = "home"))

        self.add_widget(layout)

    def register_vendor(self, instance):
        add_vendor(self.name.text, self.service_type.text, self.location.text)
        print("Vendor Registered Successfully!")
        self.manager.current = "home"

# Client Dashboard Screen
class ClientDashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=10)
        layout.add_widget(MDLabel(text="Client Dashboard", halign="center", font_style="H5"))

        layout.add_widget(MDRaisedButton(text="View Recommended Vendors", on_press=self.show_vendors))
        layout.add_widget(MDRaisedButton(text="Create Event", on_press=lambda x: self.manager.current = "create_event"))

        self.vendor_list = ScrollView()
        layout.add_widget(self.vendor_list)

        self.add_widget(layout)

    def show_vendors(self, instance):
        vendors = get_vendors()
        vendor_list_layout = MDBoxLayout(orientation="vertical", spacing=10, size_hint_y=None)
        vendor_list_layout.bind(minimum_height=vendor_list_layout.setter("height"))
        for vendor in vendors:
            vendor_list_layout.add_widget(MDLabel(text=f"{vendor[0]} - {vendor[1]} ({vendor[2]})", halign="center"))
        self.vendor_list.clear_widgets()
        self.vendor_list.add_widget(vendor_list_layout)

# Main App
class ASAEventApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(VendorScreen(name="vendor"))
        sm.add_widget(ClientDashboardScreen(name="client_dashboard"))
        return sm

if __name__ == "__main__":
    init_db()  # Initialize database
    ASAEventApp().run()
