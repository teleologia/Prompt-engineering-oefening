# Prompt Engineering Oefeningen

Dit project bevat drie eenvoudige voorbeelden van toepassingen waarbij prompts worden gebruikt om AI-modellen aan te sturen. Elke map bevat een kleine Flask-applicatie.

## Mappen

- **Prompt_engineering1** – Een webapplicatie waarin je een review kunt invoeren. Via de OpenAI API wordt de review geclassificeerd als positief, neutraal of negatief. Het resultaat wordt getoond in een gekleurde tekstbalk.
- **prompt_engineering2** – Vraagt om een beschrijving van een stemming en genereert vervolgens CSS-kleuren die daarbij passen. Deze app maakt nu gebruik van de OpenAI API.
- **prompt_engineering3** – Toont hoe je met natuurlijke taal SQL-query's kunt genereren. De gegenereerde query wordt uitgevoerd op een SQLite-database.

## Installatie

1. Installeer de vereiste pakketten:
   ```bash
   pip install -r requirements.txt
   ```
2. Maak een `.env`-bestand aan met daarin minstens de variabelen `OPENAI_API_KEY` en `OPENAI_MODEL`.
   Deze worden door alle oefeningen gebruikt om het juiste model te kiezen en de API-sleutel te laden.
3. (Optioneel) Voor project 3 kun je eerst de database aanmaken met:
   ```bash
   python prompt_engineering3/create_db.py
   ```

## Gebruik

Start een van de `app.py`-bestanden in de gewenste map om de corresponderende webapp te draaien. Bijvoorbeeld:

```bash
python Prompt_engineering1/app.py
```

Bezoek daarna `http://localhost:5000` in de browser.

