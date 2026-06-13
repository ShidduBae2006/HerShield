from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.widget import Widget
from kivy.utils import platform
from plyer import sms

# Only import Android-specific modules if running on an actual Android device
if platform == 'android':
    from android.permissions import request_permissions, Permission

class HerShieldDashboard(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        top_spacer = Widget()
        bottom_spacer = Widget()

        main_layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.status_label = MDLabel(
            text="HerShield: System Secure",
            halign="center",
            font_style="Headline",
            theme_text_color="Primary"
        )
        
        sos_btn = MDFillRoundFlatButton(
            text="TRIGGER SOS",
            font_size="24sp",
            md_bg_color=(0.9, 0.1, 0.1, 1), 
            size_hint=(0.8, None),
            height="80dp",
            pos_hint={"center_x": 0.5},
            on_release=self.trigger_sos
        )
        
        main_layout.add_widget(top_spacer)
        main_layout.add_widget(self.status_label)
        main_layout.add_widget(sos_btn)
        main_layout.add_widget(bottom_spacer)
        self.add_widget(main_layout)

    def trigger_sos(self, instance):
        self.status_label.text = "Broadcasting Emergency SMS Alerts..."
        
        emergency_contacts = ["6395589940", "7060164449"]
        message_content = "EMERGENCY ALERT from HerShield! I need help immediately! Please check my last known coordinates."
        
        try:
            for contact in emergency_contacts:
                sms.send(recipient=contact, message=message_content)
            self.status_label.text = "SOS Alerts Sent via SIM Successfully!"
        except Exception as e:
            # Captures cases where user denied the permission at runtime
            self.status_label.text = "Transmission Failed: Check Device Permissions"

class HerShieldApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        return HerShieldDashboard()

    def on_start(self):
        # Dynamically ask the user for permission as soon as the app opens
        if platform == 'android':
            request_permissions([Permission.SEND_SMS])

if __name__ == "__main__":
    HerShieldApp().run()
