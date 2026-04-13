SALES_DATA = {
    "monthly_revenue": [
        {"month": "Jan", "revenue": 124000, "target": 120000},
        {"month": "Feb", "revenue": 138000, "target": 125000},
        {"month": "Mar", "revenue": 151000, "target": 130000},
        {"month": "Apr", "revenue": 142000, "target": 135000},
        {"month": "May", "revenue": 168000, "target": 140000},
        {"month": "Jun", "revenue": 175000, "target": 145000},
        {"month": "Jul", "revenue": 159000, "target": 150000},
        {"month": "Aug", "revenue": 183000, "target": 155000},
        {"month": "Sep", "revenue": 197000, "target": 160000},
        {"month": "Oct", "revenue": 210000, "target": 165000},
        {"month": "Nov", "revenue": 228000, "target": 170000},
        {"month": "Dec", "revenue": 245000, "target": 175000},
    ],
    "active_deals": [
        {"name": "Acme Corp", "value": 48000, "stage": "Proposal", "probability": 60},
        {"name": "TechWave", "value": 92000, "stage": "Negotiation", "probability": 80},
        {"name": "BlueStar", "value": 31000, "stage": "Discovery", "probability": 30},
        {"name": "NovaBuild", "value": 67000, "stage": "Demo", "probability": 50},
        {"name": "Orion LLC", "value": 115000, "stage": "Closed-Won", "probability": 100},
    ],
    "by_region": [
        {"region": "North", "revenue": 520000},
        {"region": "South", "revenue": 390000},
        {"region": "East", "revenue": 610000},
        {"region": "West", "revenue": 480000},
    ],
    "kpis": {
        "total_revenue": 2120000,
        "active_deals": 24,
        "win_rate": 68,
        "avg_deal_size": 54000,
    },
}

INVENTORY_DATA = {
    "stock_levels": [
        {"product": "Widget A", "sku": "WA-001", "stock": 340, "reorder_point": 100, "unit_cost": 12.50},
        {"product": "Widget B", "sku": "WB-002", "stock": 87, "reorder_point": 150, "unit_cost": 18.00},
        {"product": "Gadget X", "sku": "GX-010", "stock": 512, "reorder_point": 200, "unit_cost": 34.75},
        {"product": "Gadget Y", "sku": "GY-011", "stock": 23, "reorder_point": 80, "unit_cost": 55.00},
        {"product": "Part C", "sku": "PC-020", "stock": 1200, "reorder_point": 300, "unit_cost": 4.20},
        {"product": "Part D", "sku": "PD-021", "stock": 65, "reorder_point": 100, "unit_cost": 8.90},
    ],
    "turnover_by_category": [
        {"category": "Widgets", "turnover_rate": 4.2},
        {"category": "Gadgets", "turnover_rate": 6.8},
        {"category": "Parts", "turnover_rate": 9.1},
        {"category": "Accessories", "turnover_rate": 3.5},
    ],
    "kpis": {
        "total_skus": 142,
        "low_stock_alerts": 8,
        "inventory_value": 1840000,
        "turnover_rate": 5.9,
    },
}

FINANCE_DATA = {
    "monthly_pl": [
        {"month": "Jan", "revenue": 124000, "expenses": 98000, "profit": 26000},
        {"month": "Feb", "revenue": 138000, "expenses": 104000, "profit": 34000},
        {"month": "Mar", "revenue": 151000, "expenses": 110000, "profit": 41000},
        {"month": "Apr", "revenue": 142000, "expenses": 107000, "profit": 35000},
        {"month": "May", "revenue": 168000, "expenses": 118000, "profit": 50000},
        {"month": "Jun", "revenue": 175000, "expenses": 122000, "profit": 53000},
    ],
    "expense_breakdown": [
        {"category": "Payroll", "amount": 520000},
        {"category": "Marketing", "amount": 148000},
        {"category": "Infrastructure", "amount": 92000},
        {"category": "Operations", "amount": 74000},
        {"category": "R&D", "amount": 110000},
        {"category": "Other", "amount": 56000},
    ],
    "budget_vs_actual": [
        {"dept": "Sales", "budget": 200000, "actual": 183000},
        {"dept": "Marketing", "budget": 150000, "actual": 148000},
        {"dept": "Engineering", "budget": 300000, "actual": 318000},
        {"dept": "Operations", "budget": 100000, "actual": 92000},
        {"dept": "HR", "budget": 80000, "actual": 76000},
    ],
    "kpis": {
        "total_revenue": 2120000,
        "total_expenses": 1659000,
        "net_profit": 461000,
        "profit_margin": 21.7,
    },
}

HR_DATA = {
    "headcount_by_dept": [
        {"dept": "Engineering", "headcount": 42},
        {"dept": "Sales", "headcount": 28},
        {"dept": "Marketing", "headcount": 14},
        {"dept": "Operations", "headcount": 19},
        {"dept": "HR", "headcount": 7},
        {"dept": "Finance", "headcount": 9},
    ],
    "monthly_hiring": [
        {"month": "Jan", "hired": 3, "left": 1},
        {"month": "Feb", "hired": 5, "left": 2},
        {"month": "Mar", "hired": 2, "left": 0},
        {"month": "Apr", "hired": 6, "left": 3},
        {"month": "May", "hired": 4, "left": 1},
        {"month": "Jun", "hired": 7, "left": 2},
    ],
    "tenure_distribution": [
        {"range": "0-1 yr", "count": 28},
        {"range": "1-2 yr", "count": 34},
        {"range": "2-5 yr", "count": 41},
        {"range": "5+ yr", "count": 16},
    ],
    "kpis": {
        "total_employees": 119,
        "open_positions": 11,
        "turnover_rate": 8.4,
        "avg_tenure_years": 2.8,
    },
}

DASHBOARD_KPIS = {
    "total_revenue": 2120000,
    "active_deals": 24,
    "inventory_value": 1840000,
    "total_employees": 119,
}
