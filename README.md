# PS-Band
Repo for COMP3710 - IoT BIT tour
## READ ME

### Documentation

Our artefact is called PS Band, short for 'Party Safe Band'. PS Band is a sort of tracker (like Fitbit, for example) but instead of tracking your steps, it tracks your Blood Alcohol Content (BAC). It is basically a battery powered ESP32 microcontroller which is connected to a alcohol sensor. The idea is that everyone in the group wears a PS Band, which is connected to their phone and sends the wearer’s BAC information over Bluetooth. Therefore, after implementing the server, everyone will be able to monitor their own and additionally, their friends’ BAC values.

### Software

- MacOS 10.0 or above; or Linux;
- Flutter mobile application development
- Android Studio 3.0 or later
- Espressif Integrated Development Framwork (ESP-IDF)
- Any text editor (We used VSCode)
- Xtensa architecture specific toolchain (follow the ESP-IDF installation instructions)
- Make command line utility --V

Follow the instructions [here](https://docs.espressif.com/projects/esp-idf/en/latest/get-started/index.html#setup-toolchain) to setup the toolchain for ESP32 on your preferred OS

You might also have to add the IDF-PATH to user profile. Follow the instructions [here](https://docs.espressif.com/projects/esp-idf/en/latest/get-started/add-idf_path-to-profile.html#add-idf-path-to-profile-linux-macos) for more instructions.


Follow the instructions [here](https://flutter.dev/docs/get-started/install) for installing Flutter and [here](https://flutter.dev/docs/get-started/) for setting up Android Studio to get the app development framework for this project.


### Hardware

- 1 x ESP32 microcontroller (We used NODEMCU-32S)
- 1 x Arduino microcontroller (To provide 5.0 V input to the alcohol sensor)
- 1 x MQ-3 (Alcohol sensor)
- 3 x Jumper Cables (Multi-coloured to be more diverse and inclusive)

### Licensing 
Please refer to a file named 'LICENSE' in the root directory for the licensing details.

### Contact
If you are interested in this project and would like to contribute, please get in contact with us at chinmay.garg@mail.com
