import random
from datetime import date, timedelta
import csv

random.seed(42)

KECAMATAN = [
    ("Gubeng", -7.275614, 112.750832),
    ("Sukolilo", -7.289212, 112.793726),
    ("Tambaksari", -7.258941, 112.764321),
    ("Wonokromo", -7.297842, 112.734981),
    ("Rungkut", -7.318452, 112.784512),
    ("Mulyorejo", -7.267431, 112.803124),
    ("Genteng", -7.259842, 112.742312),
    ("Tegalsari", -7.270984, 112.731245),
    ("Sawahan", -7.281342, 112.720984),
    ("Kenjeran", -7.223874, 112.768923),
]

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def generate_year(start_date: date, days: int = 365):
    # Base kondisi per kecamatan (biar realistis & konsisten)
    base = {}
    for name, lat, lon in KECAMATAN:
        base_pop = random.randint(800, 2900)
        base_ster_rate = random.uniform(0.35, 0.65)  # 35% - 65%
        base_programs = random.randint(1, 4)
        base_hotspots = random.randint(0, 3)
        base[name] = dict(
            lat=lat, lon=lon,
            pop=base_pop,
            ster_rate=base_ster_rate,
            programs=base_programs,
            hotspots=base_hotspots
        )

    # 1) kecamatan summary (snapshot terbaru)
    kec_rows = []
    for name, lat, lon in KECAMATAN:
        b = base[name]
        est = int(b["pop"])
        ster_rate_pct = round(b["ster_rate"] * 100, 2)
        kec_rows.append({
            "KECAMATAN_NAME": name,
            "ESTIMATED_CATS": est,
            "HIGH_RISK_SPOTS": int(b["hotspots"]),
            "STERILIZATION_RATE": ster_rate_pct,
            "ACTIVE_PROGRAMS": int(b["programs"]),
            "LATITUDE": lat,
            "LONGITUDE": lon,
        })

    # 2) population trends (harian per kecamatan)
    trend_rows = []
    d = start_date
    # buat state dinamis per kecamatan
    state = {}
    for name, _, _ in KECAMATAN:
        b = base[name]
        pop = b["pop"]
        sterilized = int(pop * b["ster_rate"])
        rescued = random.randint(10, 90)
        state[name] = {"pop": pop, "sterilized": sterilized, "rescued": rescued, "ster_rate": b["ster_rate"]}

    for _ in range(days):
        for name, _, _ in KECAMATAN:
            s = state[name]

            # growth harian (dipengaruhi sterilization: makin tinggi sterilization, growth makin rendah)
            base_growth = random.uniform(-0.002, 0.01)  # -0.2% s/d +1% per hari (kecil)
            ster_effect = (0.6 - s["ster_rate"]) * 0.006  # ster rendah -> growth naik sedikit
            growth_rate = base_growth + ster_effect

            # update pop
            new_pop = int(round(s["pop"] * (1 + growth_rate)))
            new_pop = clamp(new_pop, 200, 8000)

            # sterilized bertambah sedikit (program berjalan)
            ster_increase = random.randint(0, 6)
            new_ster = clamp(s["sterilized"] + ster_increase, 0, new_pop)

            # rescued fluktuatif
            rescued_delta = random.randint(-2, 4)
            new_rescued = clamp(s["rescued"] + rescued_delta, 0, 999999)

            # update ster_rate state
            new_ster_rate = new_ster / new_pop if new_pop > 0 else 0.0
            s.update(pop=new_pop, sterilized=new_ster, rescued=new_rescued, ster_rate=new_ster_rate)

            trend_rows.append({
                "DATE": d.isoformat(),
                "KECAMATAN_NAME": name,
                "TOTAL_POPULATION": int(new_pop),
                "STERILIZED": int(new_ster),
                "RESCUED": int(new_rescued),
            })

        d += timedelta(days=1)

    return kec_rows, trend_rows

if __name__ == "__main__":
    start = date(2025, 1, 1)  # ganti sesuai kebutuhan
    df_kec, df_trend = generate_year(start_date=start, days=365)

    # output ke CSV (paling gampang untuk COPY INTO)
    with open("kecamatan.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=df_kec[0].keys())
        writer.writeheader()
        writer.writerows(df_kec)

    with open("population_trends.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=df_trend[0].keys())
        writer.writeheader()
        writer.writerows(df_trend)

    print("Generated files:")
    print("- kecamatan.csv")
    print("- population_trends.csv")
    print(f"Rows: KECAMATAN={len(df_kec)}, POPULATION_TRENDS={len(df_trend)}")
