// Scrivere un semplice programma Java che apre una finestra con un pulsante.
// Quando si preme il pulsante, viene stampata la scritta "Premuto!"

import javax.swing.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

class Ascoltatore implements ActionListener {
    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println("Premuto!");
    }
}

public class Pulsante {
    public static void main(String[] args) {
        JFrame finestra = new JFrame();
        JButton premuto = new JButton("premere");
        Ascoltatore ascolta = new Ascoltatore();

        finestra.add(premuto);
        premuto.addActionListener(ascolta);

        finestra.pack();
        finestra.isVisible(true);
    }
}