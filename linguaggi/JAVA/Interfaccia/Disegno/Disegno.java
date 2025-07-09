import java.awt.BorderLayout;
import javax.swing.*;

class Disegno {
    public static void main(String args[]) {
        JFrame finestra;
        JButton cambia, diverso;
        JTextField mostra;

        finestra = new JFrame(); // crea la finestra

        cambia = new JButton("cambia"); // crea un pulsante
        finestra.add(cambia, BorderLayout.NORTH); // lo aggiunge alla finestra

        diverso = new JButton("diverso"); // altro pulsante
        finestra.add(diverso, BorderLayout.SOUTH); // aggiunta alla finestra

        mostra = new JTextField("iniziale"); // campo di testo
        finestra.add(mostra, BorderLayout.CENTER); // aggiunta alla finestra

        finestra.pack(); // adatta la finestra al contenuto
        finestra.setVisible(true); // rende la finestra visibile

        System.out.println("fine");
    }
}