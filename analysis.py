
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
layoffs_df = pd.read_csv(
    "data/tech_layoffs_hiring_trends_elite_v2.csv"
)

# Dataset Information
print("Dataset Shape:")
print(layoffs_df.shape)

print("\nColumns:")
print(layoffs_df.columns)

print("\nMissing Values:")
print(layoffs_df.isnull().sum())

print("\nDuplicate Rows:")
print(layoffs_df.duplicated().sum())

# ====================================
# Total Layoffs by Industry
# ====================================

industry_layoffs = (
    layoffs_df.groupby("industry")["layoffs_count"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTotal Layoffs by Industry")
print(industry_layoffs)

# Industry Layoffs Chart

industry_layoffs.plot(kind="bar")

plt.title("Total Layoffs by Industry")
plt.xlabel("Industry")
plt.ylabel("Total Layoffs")

plt.tight_layout()

plt.savefig("industry_layoffs.png")

plt.show()
plt.savefig("industry_layoffs.png")

# ====================================
# Total Layoffs by Country
# ====================================

country_layoffs = (
    layoffs_df.groupby("country")["layoffs_count"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTotal Layoffs by Country")
print(country_layoffs)

# Country Layoffs Chart

country_layoffs.plot(kind="bar")

plt.title("Total Layoffs by Country")
plt.xlabel("Country")
plt.ylabel("Total Layoffs")

plt.tight_layout()

plt.savefig("country_layoffs.png")

plt.show()
# ====================================
# Top 10 Companies by Layoffs
# ====================================

top_companies = (
    layoffs_df.groupby("company_name")["layoffs_count"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Companies by Layoffs")
print(top_companies)
# Top Companies Chart

top_companies.plot(kind="bar",color="green")

plt.title("Top 10 Companies by Layoffs")
plt.xlabel("Company")
plt.ylabel("Total Layoffs")

plt.tight_layout()

plt.savefig("top_companies.png")

plt.show()

# ====================================
# Layoffs by Year
# ===================================
# ====================================
# Layoffs by Year
# ====================================

yearly_layoffs = (
    layoffs_df.groupby("year")["layoffs_count"]
    .sum()
    .sort_values()
)

print("\nLayoffs by Year")
print(yearly_layoffs)

# Yearly Layoffs Chart

yearly_layoffs.plot(
    kind="bar",
    color="purple"
)

plt.title("Total Layoffs by Year")
plt.xlabel("Year")
plt.ylabel("Total Layoffs")

plt.tight_layout()

plt.savefig("yearly_layoffs.png")

plt.show()