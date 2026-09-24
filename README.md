# Système Intelligent de Pilotage des Performances Commerciales

Projet de Fin d'Année (PFA) — Ingénieur Génie Industriel, Option Business & Data Management
**ESITH** | Réalisé auprès de la **Banque Populaire — Siège Régional Marrakech Béni Mellal** (été 2026)

Par **Adam Benmoussa**

---

## ⚠️ Note sur les données

Ce projet a été réalisé dans un contexte bancaire réel, mais **aucune donnée client ou d'agence réelle n'est publiée dans ce dépôt**. Le système a été développé et démontré à partir de deux mois de données réelles rigoureusement anonymisées (noms d'agences et de clients remplacés), complétées par des données synthétiques générées en Python reproduisant fidèlement la même structure. Seules ces données anonymisées/synthétiques figurent ici, à des fins de démonstration méthodologique.

## 🎯 Contexte et problématique

Au sein de la Direction Commerciale de la région, le pilotage de la performance de **17 agences** reposait sur des extractions manuelles depuis Oracle, sans dashboard consolidé, avec une visibilité sur les objectifs disponible **uniquement en fin de mois**.

> Comment automatiser la collecte et le traitement des données commerciales, et exploiter l'intelligence artificielle, afin de fournir à la Direction Commerciale une visibilité en temps réel et anticipée sur la performance des agences de la région ?

## 🏗️ Architecture — 5 couches

| Layer | Description | Techs |
|---|---|---|
| **0 — Préparation des données** | Données réelles anonymisées + données synthétiques complémentaires (6 mois d'historique) | Python (pandas, numpy, openpyxl) |
| **1 — Pipeline d'automatisation** | Lecture de fichiers Excel bruts complexes, nettoyage, calcul des KPIs (TRO, classements) | Python (pandas, scikit-learn) |
| **2 — Tableau de bord** | Dashboard interactif à 5 pages (Vue Globale, Suivi Crédit, Performance Produits, Activité Journalière, Benchmark Régional) | Power BI (DAX, Power Query) |
| **3 — Modèle prédictif** | Détection dès le milieu du mois des agences à risque | KNIME Analytics Platform, H2O AutoML (Random Forest) |
| **4 — Alertes automatisées** | Rapport hebdomadaire par email au directeur régional, recommandations générées par IA | n8n (self-hosted), Ollama / LLaMA 3.2, Gmail API |

## 📊 Résultats clés

- **Accuracy du modèle prédictif : 88,2 %** (Random Forest standard), Kappa de Cohen = 0,765
- Détection des agences à risque **dès le milieu du mois** au lieu de la fin de mois
- Rapport hebdomadaire automatique envoyé chaque lundi 8h, sans action manuelle
- Passage d'un reporting **manuel et rétrospectif** à un pilotage **automatisé, prédictif et proactif**

## 📁 Structure du dépôt

```
├── data/
│   └── synthetic/              # Données anonymisées/synthétiques (aucune donnée réelle)
├── python/
│   ├── layer0_data_prep/       # Génération et anonymisation des données
│   └── layer1_pipeline/        # Nettoyage, restructuration, calcul des KPIs
├── knime/
│   └── credit_prediction.knwf  # Workflow KNIME (Random Forest / H2O)
├── powerbi/
│   └── dashboard.pbix          # Tableau de bord (5 pages)
├── n8n/
│   └── weekly_alert_workflow.json
├── docs/
│   ├── rapport_pfa.pdf         # Rapport complet
│   └── screenshots/            # Captures du dashboard, du workflow, etc.
└── README.md
```

## 🛠️ Stack technique

Python · pandas · scikit-learn · Power BI · KNIME Analytics Platform · H2O AutoML · n8n · Ollama (LLaMA 3.2) · Gmail API

## 📄 Rapport complet

Le rapport détaillé (contexte, méthodologie, analyse des causes, résultats) est disponible dans [`docs/rapport_pfa.pdf`](docs/rapport_pfa.pdf).

## 👤 Auteur

**Adam Benmoussa** — ESITH, Ingénieur Génie Industriel, Option Business & Data Management
