from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.widget import Widget
from plyer import sms

class HerShieldDashboard(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        top_spacer = Widget()
        bottom_spacer = Widget()

        main_layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.status_label = MDLabel(
            text="HerShield: System Secure",
            halign="center",
            font_style="H5",
            theme_text_color="Primary"
        )
        
        sos_btn = MDRaisedButton(
            text="TRIGGER SOS",
            font_size="24sp",
            md_bg_color=(0.9, 0.1, 0.1, 1), 
            size_hint=(0.8, 0.2),
            pos_hint={"center_x": 0.5},
            on_release=self.trigger_sos
        )
        
        main_layout.add_widget(top_spacer)
        main_layout.add_widget(self.status_label)
        main_layout.add_widget(sos_btn)
        main_layout.add_widget(bottom_spacer)
        self.add_widget(main_layout)

    def trigger_sos(self, instance):
        # Clear, standard text string with NO emojis to prevent encoding crashes
        self.status_label.text = "Broadcasting Emergency SMS Alerts..."
        
        emergency_contacts = ["6395589940", "7060164449"]
        message_content = "EMERGENCY ALERT from HerShield! I need help immediately! Please check my last known coordinates."
        
        try:
            for contact in emergency_contacts:
                sms.send(recipient=contact, message=message_content)
            self.status_label.text = "SOS Alerts Sent via SIM Successfully!"
        except Exception as e:
            self.status_label.text = "Transmission Failed: Check Device Hardware"

class HerShieldApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        return HerShieldDashboard()

if __name__ == "__main__":
    HerShieldApp().run()