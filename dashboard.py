import streamlit as st
import pandas as pd

# Dati estratti dal PDF
data = {
    "Lunedì": {
        "Colazione": "2 pesche/5 susine, 2 pancakes milk pro, Home-made, 2 cucchiaini di miele/marmellata",
        "Spuntino 1": "Frullato con: 250ml latte di mandorla/avena, 20g proteine whey, 1 banana/50g mirtilli",
        "Spuntino 2": "30g mandorle/noci/nocciole/anacardi",
        "Pranzo": "300g melone cantalupo, 100g prosciutto crudo, 6 grissini integrali/al sesamo",
        "Cena": "Club sandwich con: 300g petti di pollo, 150g pomodorini, 100g cetriolo/lattuga, 3 cucchiai di maionese, 100g pane di segale/multicereali, 15g olio evo"
    },
    "Martedì": {
        "Colazione": "Succo di 2 limoni diluiti in 1 bicchiere d’acqua, 80g pane di segale, 2 uova strapazzate, 2 cucchiaini di miele",
        "Spuntino 1": "300g anguria/melone cantalupo, 50g galbanino/belpaese",
        "Spuntino 2": "30g mandorle/noci/nocciole/anacardi",
        "Pranzo": "2 piadine integrali/mais da 120g con dentro ciascuna: 150g mozzarella di bufala, 50g pomodorini, 50g lattuga/songino, 5g olio evo",
        "Cena": "Involtini con: 150g bresaola/carpaccio di manzo, 200g philadelphia/robiola/crescenza, 300g zucchine/peperoni, 100g pane di segale/multicereali, 15g olio evo"
    },
    "Mercoledì": {
        "Colazione": "250ml latte di mandorla/avena, 25g proteine whey, 80g pane di segale, crema di nocciole/pistacchio a raso, 1 banana a rondelle",
        "Spuntino 1": "1 barretta proteica da 40g, 15 ciliegie/2 pere estive",
        "Spuntino 2": "30g mandorle/noci/nocciole/anacardi",
        "Pranzo": "150g pasta integrale, 100g mais sgocciolato, 5 olive, 200g pomodorini, 100g tonno in boccia",
        "Cena": "Omelette con: 3 uova strapazzate, 50g prosciutto crudo, 200g pomodorini, 100g pane di segale/multicereali, 10g olio evo"
    },
    "Giovedì": {
        "Colazione": "Succo di 2 limoni diluiti in 1 bicchiere d’acqua, 80g pane di segale, 2 uova strapazzate, 2 cucchiaini di miele",
        "Spuntino 1": "300g anguria/melone cantalupo, 50g galbanino/belpaese",
        "Spuntino 2": "30g mandorle/noci/nocciole/anacardi",
        "Pranzo": "2 piadine integrali/mais da 120g con dentro ciascuna: 150g philadelphia, 50g pomodorini, 50g lattuga/songino, 5g olio evo",
        "Cena": "Involtini con: 150g fesa di tacchino/prosciutto crudo, 200g philadelphia/robiola/crescenza, 300g zucchine/peperoni, 100g pane di segale/multicereali, 15g olio evo"
    },
    "Venerdì": {
        "Colazione": "2 pesche/5 susine, 2 pancakes milk pro, Home-made, 2 cucchiaini di miele/marmellata",
        "Spuntino 1": "1 barretta proteica da 40g, 15 ciliegie/2 pere estive",
        "Spuntino 2": "30g mandorle/noci/nocciole/anacardi",
        "Pranzo": "130g riso basmati/venere, 100g mais sgocciolato, 5 olive, 200g pomodorini, 100g tonno in boccia",
        "Cena": "300g pesce fresco/400g surgelato, 150g cetriolo/lattuga, 3 cucchiai di maionese, 100g pane di segale/multicereali, 15g olio evo"
    },
    "Sabato": {
        "Colazione": "Succo di 2 limoni diluiti in 1 bicchiere d’acqua, 80g pane di segale, 2 uova strapazzate, 2 cucchiaini di miele",
        "Spuntino 1": "Frullato con: 250ml latte di mandorla/avena, 20g proteine whey, 1 banana/50g mirtilli",
        "Spuntino 2": "30g mandorle/noci/nocciole/anacardi",
        "Pranzo": "Bruschetta con: 220g pane di segale/casereccio tostato, 3 cucchiaini di pesto genovese, 200g pomodorini, 150g burrata, 5 olive",
        "Cena": "Libero"
    }
}

# Creazione della sidebar per la selezione del giorno
st.sidebar.title("Seleziona il giorno")
giorno = st.sidebar.selectbox("Giorno", list(data.keys()))

# Visualizzazione dei pasti
st.title(f"Regime alimentare per {giorno}")
for pasto, descrizione in data[giorno].items():
    st.header(pasto)
    st.write(descrizione)
