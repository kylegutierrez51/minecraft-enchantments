# Minecraft Enchantment Data

A simple web app used to show basic data on Minecraft Enchantments. This features data such as enchantment category, max level, weight (rarity), treasure only, and version added.

`Treasure only` refers to enchantments that cannot be obtained from enchanting tables.

## Dataset

The `data.json` file comes from `https://api.astroworldmc.com/`




## Setup
1. Ensure you have Python 3.x installed
2. Clone the repository: 
   ```bash
   git clone https://github.com/kylegutierrez51/minecraft-enchantments.git
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the Streamlit App
   ```bash
   streamlit run main.py
   ```