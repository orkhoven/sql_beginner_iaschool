import streamlit as st
import pandas as pd

# ======================
# Data Preparation
# ======================

products_data = [
    [1, "Laptop", "Electronics", 899.99],
    [2, "Smartphone", "Electronics", 699.99],
    [3, "Headphones", "Electronics", 149.99],
    [4, "Coffee Maker", "Home Appliances", 89.99],
    [5, "Blender", "Home Appliances", 59.99],
    [6, "Book: Python Basics", "Books", 29.99],
    [7, "Office Chair", "Furniture", 149.00],
    [8, "Desk Lamp", "Furniture", 49.00],
    [9, "Gaming Mouse", "Electronics", 79.99],
    [10, "Smartwatch", "Electronics", 199.99]
]

sales_data = [
    [1, "2024-03-01", 1, 1, 899.99],
    [2, "2024-03-01", 3, 2, 299.98],
    [3, "2024-03-01", 5, 3, 179.97],
    [4, "2024-03-02", 2, 1, 699.99],
    [5, "2024-03-02", 6, 4, 119.96],
    [6, "2024-03-02", 7, 2, 298.00],
    [7, "2024-03-03", 10, 1, 199.99],
    [8, "2024-03-03", 9, 5, 399.95],
    [9, "2024-03-03", 4, 1, 89.99],
    [10, "2024-03-04", 8, 3, 147.00]
]

products_df = pd.DataFrame(products_data, columns=["product_id", "product_name", "category", "unit_price"])
sales_df = pd.DataFrame(sales_data, columns=["sale_id", "sale_date", "product_id", "quantity", "total_price"])

# ======================
# Expected Answers (normalized lowercase, stripped)
# ======================

answers = {
    1: "select * from sales;",
    2: "select product_name, unit_price from products;",
    3: "select sale_id, sale_date from sales;",
    4: "select * from sales where total_price > 100;",
    5: "select * from products where category = 'electronics';",
    6: "select sale_id, total_price from sales where sale_date = '2024-03-01';",
    7: "select product_id, product_name from products where unit_price > 100;",
    8: "select sum(total_price) from sales;",
    9: "select avg(unit_price) from products;",
    10: "select sum(quantity) from sales;",
    11: "select sale_date, count(*) from sales group by sale_date;",
    12: "select * from products order by unit_price desc limit 1;",
    13: "select * from sales where quantity > 4;",
    14: "select * from products order by unit_price desc;",
    15: "select round(sum(total_price), 2) from sales;",
    16: "select avg(total_price) from sales;",
    17: "select date_format(sale_date, '%Y-%m-%d') from sales;",
    18: "select sum(s.total_price) from sales s join products p on s.product_id = p.product_id where p.category = 'electronics';",
    19: "select * from products where unit_price between 20 and 600;",
    20: "select product_name, category from products order by category;"
}

# ======================
# Streamlit Interface
# ======================

st.set_page_config(page_title="SQL Exercises", layout="wide")
st.title("SQL Exercises – Products & Sales Dataset")

st.subheader("Table: Products")
st.dataframe(products_df, use_container_width=True)

st.subheader("Table: Sales")
st.dataframe(sales_df, use_container_width=True)

st.markdown("---")
st.header("SQL Query Exercises")

questions = [
    "1. Récupérez toutes les colonnes du tableau Sales.",
    "2. Récupérez product_name et unit_price du tableau Products.",
    "3. Récupérez sale_id et sale_date du tableau Sales.",
    "4. Filtrez Sales pour total_price > 100 $.",
    "5. Filtrez Products dans la catégorie « Electronics ».",
    "6. Récupérer sale_id et total_price pour les ventes du 03/01/2024.",
    "7. Récupérer product_id et product_name pour les produits dont le prix est > 100 $.",
    "8. Calculer le revenu total de toutes les ventes.",
    "9. Calculer le prix unitaire moyen des produits.",
    "10. Calculer la quantité totale vendue à partir de Sales.",
    "11. Compter les ventes par jour.",
    "12. Produit avec le prix unitaire le plus élevé.",
    "13. Ventes avec quantité vendue > 4.",
    "14. Liste des produits classés par prix décroissant.",
    "15. Prix total de toutes les ventes, arrondi à 2 décimales.",
    "16. Prix total moyen des ventes.",
    "17. Formater la date de vente au format AAAA-MM-JJ.",
    "18. Revenu total pour la catégorie « Électronique ».",
    "19. Récupérer les produits dont le prix est compris entre 20 et 600 dollars.",
    "20. Répertorier le nom du produit et la catégorie par ordre de catégorie."
]

for i, q in enumerate(questions, start=1):
    st.markdown(f"**{q}**")
    answer_input = st.text_area("Votre requête SQL :", key=f"q{i}", height=60)
    if answer_input.strip().lower().replace(";", "") == answers[i].replace(";", ""):
        st.success("✅ Correct")
    else:
        st.info("En attente ou incorrect")

st.markdown("---")
st.caption("Les réponses sont vérifiées automatiquement par comparaison textuelle simple.")

