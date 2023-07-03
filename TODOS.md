## Schritt 1.1 - Spielfeld:

### 1. Erstellen des Spielfelds:
   - Definieren der Größe des Spielfelds, zum Beispiel als Anzahl von Zeilen und Spalten.
   - Erstellen einer Datenstruktur, um das Spielfeld zu repräsentieren. Eine mögliche Option ist ein zweidimensionales Array oder eine Liste von Listen.
   - Initialisieren des Spielfelds mit leeren Zellen. Das kann beispielsweise durch das Setzen aller Elemente des Arrays auf einen bestimmten Wert oder das Erstellen einer entsprechenden Datenstruktur erreicht werden.

### 2. Aktualisieren des Spielfelds:
   - Definieren der Regeln, nach denen sich die Sandpartikel bewegen und interagieren sollen. Zum Beispiel könnten Regeln festlegen, dass ein Sandpartikel nach unten fällt, wenn darunter eine leere Zelle ist, oder dass Sandpartikel
     horizontal rollen, wenn sie genügend "Schwung" haben.
   - Implementieren einer Funktion, die das Spielfeld aktualisiert, indem sie die Regeln auf die vorhandenen Sandpartikel anwendet. Diese Funktion sollte das Spielfeld entsprechend den Regeln aktualisieren und gegebenenfalls den 
     neuen Zustand zurückgeben.

### 3. Setzen von Sandpartikeln (und später anderen "Objekten" -> z.B Hindernisse):
   - Implementieren einer Funktion, die es dem Benutzer ermöglicht, Sandpartikel an bestimmten Positionen auf dem Spielfeld zu platzieren. Diese Funktion könnte die Position des Sandpartikels als Parameter erhalten und das 
     entsprechende Element im Spielfeld entsprechend setzen.

### 4. Bewegen von Sandpartikeln:
   - Implementieren der Logik, um Sandpartikel auf dem Spielfeld zu bewegen. Dies kann automatisch durch bestimmte Regeln gesteuert werden.
   - Bei automatischer Bewegung, sollte man eine Funktion erstellen, die das gesamte Spielfeld durchläuft und die Regeln auf jedes Sandpartikel anwendet, um ihre Bewegung zu bestimmen. (Oder zumindest diejenigen Partikel updaten, 
     bei denen sich zur nächsten Generation der 'state' verändert.)

### 5. Anzeigen des Spielstands:
   - Entscheiden, wie der aktuelle Zustand des Spielfelds angezeigt werden soll. Dies kann textbasiert durch Ausgabe in der Konsole (Testing / Bugfixing) oder grafisch (in eigener APP) durch eine Benutzeroberfläche erfolgen.
   - Implementieren der entsprechenden Funktionen, die den Spielstand auf die gewünschte Weise darstellen. Für edie grafische Darstellung, könnten Bibliotheken wie Pygame oder Tkinter eine geeignete Kandidaten sein.
