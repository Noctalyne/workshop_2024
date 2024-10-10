# Simulation de recolte de données du bracelet

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def generate_blood_pressure_data(num_readings=144):  # 144 readings for every 10 minutes in a day
    np.random.seed(5)  # Pour la reproductibilité
    # Générer des données de pression artérielle normale
    systolic = np.random.normal(120, 10, num_readings) # plus ou moins 10
    diastolic = np.random.normal(80, 5, num_readings) # plus ou moins 5

    # Ajouter du bruit pour simuler des variations
    systolic += np.random.normal(0, 5, num_readings)
    diastolic += np.random.normal(0, 3, num_readings)

    # Créer un DataFrame pandas
    timestamps = [datetime.now() - timedelta(minutes=i) for i in range(num_readings - 1, -1, -1)]
    #timestamps = [datetime.now() - timedelta(minutes=i) for i in range(num_readings - 1, -1, -1)]
    # timedelta represents a duration
        #exemple comme output
        #datetime(2024, 10, 8, 11, 55),  # 5 minutes ago
        #datetime(2024, 10, 8, 11, 56),  # 4 minutes ago
        #datetime(2024, 10, 8, 11, 57),  # 3 minutes ago
        #datetime(2024, 10, 8, 11, 58),  # 2 minutes ago
        #datetime(2024, 10, 8, 11, 59),  # 1 minute ago
        #datetime(2024, 10, 8, 12, 0),   # now
    df = pd.DataFrame({'timestamp': timestamps, 'systolic': systolic, 'diastolic': diastolic})

    return df

# Générer des données de pression artérielle
blood_pressure_data = generate_blood_pressure_data()

# Afficher les premières lignes des données
print(blood_pressure_data.head())

"""## 2- Fonction pour générer des données de pression artérielle avec anomalies"""

# Fonction pour générer des données de pression artérielle avec anomalies
def generate_blood_pressure_data_with_anomalies(num_readings=144):
    np.random.seed(5)  # Pour la reproductibilité
    systolic = np.random.normal(120, 10, num_readings)  # Pression systolique moyenne
    diastolic = np.random.normal(80, 5, num_readings)   # Pression diastolique moyenne

    # Ajouter du bruit pour simuler des variations naturelles
    systolic += np.random.normal(0, 5, num_readings)
    diastolic += np.random.normal(0, 3, num_readings)

    # Ajouter des anomalies intentionnelles (valeurs extrêmes)
    anomalies_systolic = [200, 195, 210]  # Anomalies systoliques élevées
    anomalies_diastolic = [120, 115, 130]  # Anomalies diastoliques élevées

    # Insérer les anomalies dans les données
    for i in range(len(anomalies_systolic)):
        if i * 10 < num_readings:  # Vérifie que l'indice est dans les limites
            systolic[i * 10] = anomalies_systolic[i]  # Remplacer une valeur toutes les 10 lectures
            diastolic[i * 10] = anomalies_diastolic[i]  # Remplacer une valeur toutes les 10 lectures

    # Créer un DataFrame pandas avec les timestamps
    timestamps = [datetime.now() - timedelta(minutes=i) for i in range(num_readings - 1, -1, -1)]
    df = pd.DataFrame({'timestamp': timestamps, 'systolic': systolic, 'diastolic': diastolic})

    return df

# Détection des anomalies
def detect_anomalies(data, threshold=3):
    anomalies = []

    # Calculer les statistiques pour systolique et diastolique
    mean_systolic = np.mean(data['systolic'])
    std_systolic = np.std(data['systolic'])
    mean_diastolic = np.mean(data['diastolic'])
    std_diastolic = np.std(data['diastolic'])

    # Détecter les anomalies en fonction du seuil (z-score > threshold)
    for index, row in data.iterrows():
        if (abs(row['systolic'] - mean_systolic) > threshold * std_systolic or
            abs(row['diastolic'] - mean_diastolic) > threshold * std_diastolic):
            anomalies.append(row)

    return pd.DataFrame(anomalies)

# Stocker les anomalies dans une base de données SQLite
def store_anomalies_in_db(anomalies, db_name='db.sqlite3'):
    # Connexion à la base de données SQLite
    conn = sqlite3.connect(db_name)

    # Vérifier si des anomalies ont été détectées
    if anomalies.empty:
        print("No anomalies detected, nothing to store.")
        conn.close()  # Close the connection if there are no anomalies
        return

    try:
        # Stocker les anomalies dans la base de données SQLite
        anomalies.to_sql('anomalies', conn, if_exists='append', index=False)

        print(f"Anomalies stored in database {db_name}.")
    except Exception as e:
        print(f"Error while inserting anomalies: {e}")
    finally:
        # Fermer la connexion
        conn.commit()
        conn.close()

# Exemple d'utilisation
if __name__ == "__main__":
    # Générer des données de pression artérielle avec des anomalies
    blood_pressure_data = generate_blood_pressure_data_with_anomalies()

    # Détecter les anomalies
    anomalies = detect_anomalies(blood_pressure_data)

    # Afficher les anomalies détectées
    print("Anomalies détectées :")
    print(anomalies)

    # Stocker les anomalies dans la base de données
    store_anomalies_in_db(anomalies)

"""## 3- Enregistrer les anomalies dans un fichier excel"""

# Function to save anomalies from the SQLite database to an Excel file
def save_anomalies_to_excel(db_name='blood_pressure_anomalies.db', excel_file='anomalies.xlsx'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)

    # Read the anomalies data into a DataFrame
    anomalies_df = pd.read_sql_query("SELECT * FROM anomalies", conn)

    # Save the DataFrame to an Excel file
    anomalies_df.to_excel(excel_file, index=False, engine='openpyxl')

    print(f"Anomalies saved to {excel_file}.")

    # Close the database connection
    conn.close()

# Assuming the generate_blood_pressure_data_with_anomalies() function generates data
def generate_blood_pressure_data_with_anomalies():
    # Placeholder function to generate dummy blood pressure data with anomalies
    data = pd.DataFrame({
        'patient_id': [1, 2, 3, 4, 5],
        'systolic': [120, 180, 115, 140, 200],  # 180 and 200 are anomalies
        'diastolic': [80, 95, 75, 85, 110]  # 95 and 110 are anomalies
    })
    return data

# Assuming the detect_anomalies() function detects anomalies in the blood pressure data
def detect_anomalies(data):
    # Simple rule: systolic > 160 or diastolic > 100 is considered an anomaly
    anomalies = data[(data['systolic'] > 160) | (data['diastolic'] > 100)]
    return anomalies

# Main block
if __name__ == "__main__":
    # Generate blood pressure data with anomalies
    blood_pressure_data = generate_blood_pressure_data_with_anomalies()

    # Detect anomalies
    anomalies = detect_anomalies(blood_pressure_data)

    # Display the detected anomalies
    print("Detected anomalies:")
    print(anomalies)

    # Save anomalies DataFrame to SQLite (for the purpose of this example, we save it into a new DB)
    conn = sqlite3.connect('blood_pressure_anomalies.db')
    anomalies.to_sql('anomalies', conn, if_exists='replace', index=False)
    conn.close()

    # Save the anomalies to an Excel file
    save_anomalies_to_excel()

    # Sauvegarder le fichier localement (il sera disponible dans le répertoire courant)
    print(f"Le fichier Excel a été sauvegardé sous le nom 'anomalies.xlsx' dans le répertoire courant.")

"""## 4- Afficher les anomalies dans un graphe"""

# Load the data from the Excel file
file_path = 'anomalies.xlsx'  # Make sure the path is correct
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Standard blood pressure values
num_readings = len(df)
systolic_standard = np.random.normal(120, 10, num_readings)  # Mean 120, std deviation 10
diastolic_standard = np.random.normal(80, 5, num_readings)   # Mean 80, std deviation 5

# Set up the bar chart
bar_width = 0.35
x = df['patient_id']

# Create the bar chart
plt.bar(x - bar_width/2, df['systolic'], width=bar_width, label='Systolic', color='orange')
plt.bar(x + bar_width/2, df['diastolic'], width=bar_width, label='Diastolic', color='green')

# Add reference lines for standard values
plt.axhline(y=120, color='blue', linestyle='--', label='Systolic Standard (120 mm Hg)')
plt.axhline(y=80, color='red', linestyle='--', label='Diastolic Standard (80 mm Hg)')

# Add titles and labels
plt.title('Blood Pressure Readings (Bar Chart)')
plt.xlabel('Patient ID')
plt.ylabel('Pressure (mm Hg)')
plt.xticks(x)
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

