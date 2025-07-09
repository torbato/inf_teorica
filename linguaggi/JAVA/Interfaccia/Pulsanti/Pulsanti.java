import java.awt.BorderLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.*;

class AzioneCambia implements ActionListener {
	JTextField testo;

	@Override
	public void actionPerformed(ActionEvent e) {
		testo.setText("cambiato");
	}
}

class AzioneDiverso implements ActionListener {
	JTextField testo;

	@Override
	public void actionPerformed(ActionEvent e) {
		testo.setText("diverso");
	}
}

class Pulsanti {
	public static void main(String args[]) {
		JFrame finestra;
		JButton cambia, diverso;
		JTextField mostra;
		AzioneCambia ac;
		AzioneDiverso ar;

		finestra = new JFrame();			// crea la finestra

		cambia = new JButton("cambia");			// crea un pulsante
		finestra.add(cambia, BorderLayout.NORTH);	// lo aggiunge alla finestra

		diverso = new JButton("diverso");		// altro pulsante
		finestra.add(diverso, BorderLayout.SOUTH);

		mostra = new JTextField("iniziale");		// campo di testo
		finestra.add(mostra, BorderLayout.CENTER);	// -> finestra

		ac = new AzioneCambia();			// reazione alla pressione
		ac.testo = mostra;				// sul primo pulsante
		cambia.addActionListener(ac);

		ar = new AzioneDiverso();			// sul secondo
		ar.testo = mostra;
		diverso.addActionListener(ar);

		finestra.pack();
		finestra.setVisible(true);
		finestra.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		System.out.println("fine");
	}
}