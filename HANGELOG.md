# Change Log

## [1.1.0] - 2024-06-10

### Added
- **Hexadezimale Ausgabe:** RGB-Werte im API-Befehl werden nun als Hexadezimalwerte ausgegeben.

### Changed
- **Neue Funktion `rgb_to_hex`:** 
  - Eine Hilfsfunktion `rgb_to_hex(color)` wurde hinzugefügt, um RGB-Werte in Hexadezimalwerte zu konvertieren.
  ```python
  def rgb_to_hex(color):
      return f"{color[0]:02x}{color[1]:02x}{color[2]:02x}"

- **Anpassung der update_matrix-Funktion:**

- Die Funktion wurde modifiziert, um Farben im API-Befehl als Hexadezimalwerte auszugeben für besere Performance in WLED.

[1.0.0] - 2023-03-23

### Added
- **Erstellung der GUI:**
- Erstellung einer GUI mit Tkinter zur Erstellung von Pixelart für eine 16x16-Matrix
- Erstellung einer 16x16-Matrix zur Speicherung von Farben.
- Erstellung Möglichkeit zur Auswahl von Farben für einzelne Pixel.
- **Bildverarbeitung:**
- Hochladen und Verarbeiten von Bildern zur Extraktion von Pixelwerten.
- Skalieren von Bildern auf 16x16 Pixel

- **API-Befehl:**
- Ausgabe der Pixel Matrix als JSON API-Befehl in Dezimalwerten.
