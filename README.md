## Etude de la détection automatique de caractéristiques sur un signal audio
![Démonstration](src/imgs/demo.png)

* [Compte-rendu en ligne](/Compte-rendu.ipynb).
* [Documentation](https://lowlighter.github.io/sound/docs/)

## Liste des fonctions disponibles

Vous trouverez ci-dessous une liste contenant les différentes fonctions implémentées.

| Nom de la fonction | Description |
| -------- | ----------- |
|| **Traitement d'un signal audio** |
| [compute](https://lowlighter.github.io/sound/docs/_bin/compute.html) | Ouvre un fichier, génère une banque de filtre, utilise un compresseur audio (facultatif) et affiche le spectre d'amplitude et le spectrogramme personnalisé |
| [compare](https://lowlighter.github.io/sound/docs/_bin/compare.html) | Compare plusieurs fichiers audios (via la fonction **compute**) |
| [live_record](https://lowlighter.github.io/sound/docs/_bin/live_record.html) | Traite les données reçus par le microphone de l'ordinateur *(nécessite pyaudio)* |
|| **Propriétés du signal audio** |
| [player](https://lowlighter.github.io/sound/docs/_bin/player.html) | Lecteur audio |
| [plot_specamp](https://lowlighter.github.io/sound/docs/_bin/plot_specamp.html) | Spectre d'amplitude |
| [plot_dbfs](https://lowlighter.github.io/sound/docs/_bin/plot_dbfs.html) | Spectre dB FS |
| [plot_specgram](https://lowlighter.github.io/sound/docs/_bin/plot_specgram.html) | Spectrogramme |
| [plot_avggram](https://lowlighter.github.io/sound/docs/_bin/plot_avggram.html) | Spectrogramme (moyenne) |
| [plot_nspecgram](https://lowlighter.github.io/sound/docs/_bin/plot_fft.html) | Spectrogramme natif |
| [plot_formants](https://lowlighter.github.io/sound/docs/_bin/plot_formatns.html) | Ajoute les formants connus sur une figure existante |
|| **Compresseur audio** |
| [drc](https://lowlighter.github.io/sound/docs/_bin/drc.html) | Applique un compresseur audio à un signal |
| [drcz](https://lowlighter.github.io/sound/docs/_bin/drcz.html) | Réponse linéaire d'un compresseur audio |
|| **Convertisseur analogique numérique** |
| [adc](https://lowlighter.github.io/sound/docs/_bin/adc.html) | Numérise un signal |
|| **Filtres et banque de filtres** |
| [bandpass](https://lowlighter.github.io/sound/docs/_bin/bandpass.html) | Génère un filtre |
| [gen_filters](https://lowlighter.github.io/sound/docs/_bin/gen_filters.html) | Génère une banque de filtre |
| [plot_freqz](https://lowlighter.github.io/sound/docs/_bin/plot_freqz.html) | Réponse fréquentielle d'une banque de filtre |
| [gen_filtered](https://lowlighter.github.io/sound/docs/_bin/gen_filtered.html) | Filtre un signal par une banque de filtre |
| [plot_filtered](https://lowlighter.github.io/sound/docs/_bin/plot_filtered.html) | Affiche un signal filtré par une banque de filtre |
|| **Energie d'un signal** |
| [energy](https://lowlighter.github.io/sound/docs/_bin/energy.html) | Calcule l'énergie d'un signal (un seul segment temporel) |
| [energies](https://lowlighter.github.io/sound/docs/_bin/energies.html) | Calcule l'énergie d'un signal (segments temporel espacés uniformément) |
| [plot_energies](https://lowlighter.github.io/sound/docs/_bin/plot_energies.html) | Affiche l'énergie d'un signal (segments temporel espacés uniformément) |
|| **Spectrogramme personnalisé d'un signal** |
| [gen_data](https://lowlighter.github.io/sound/docs/_bin/gen_data.html) | Génère les données du spectrogramme personnalisé |
| [plot_datagram](https://lowlighter.github.io/sound/docs/_bin/plot_datagram.html) | Affiche le spectrogramme personnalisé |
| [plot_data](https://lowlighter.github.io/sound/docs/_bin/plot_data.html) | Affiche le spectre d'amplitude et le spectrogramme personnalisé |
|| **Etude d'un signal** |
| [gen_sine](https://lowlighter.github.io/sound/docs/_bin/gen_sine.html) | Génère un signal sinusoïdal |
| [similar](https://lowlighter.github.io/sound/docs/_bin/similar.html) | Corrélation entre deux signaux |
| [similarities](https://lowlighter.github.io/sound/docs/_bin/similarities.html) | Corrélation entre plusieurs signaux (via la fonction compare) |
| [learning](https://lowlighter.github.io/sound/docs/_bin/learning.html) | Entraine et teste un Perceptron multicouche (Multi-layer Perceptron classifier) |
|| **Manipulation d'un signal** |
| [state_at](https://lowlighter.github.io/sound/docs/_bin/state_at.html) | Lit la valeur d'un spectrogramme personnalisé pour un filtre et un instant donné |
| [cut](https://lowlighter.github.io/sound/docs/_bin/cut.html) | Découpe un spectrogramme personnalisé en sections |
| [to1D](https://lowlighter.github.io/sound/docs/_bin/to1D.html) | Normalise un spectrogramme personnalisé en un tableau unidimensionnel |
|| **Banc de tests** |
| [benchmark](https://lowlighter.github.io/sound/docs/_bin/benchmark.html) | Effectue un banc de tests |
