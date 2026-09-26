import polars as pl

df_energy = pl.DataFrame({
    "timestamp": ["2026-09-01 00:00", "2026-09-01 01:00", "2026-09-01 02:00"],
    "price_eur_per_mwh": [45.0, 52.5, 38.0],
    "is_active": [True, True, False],
})

selected_df = df_energy.select([
    pl.col("is_active"),
    pl.col("price_eur_per_mwh").alias("spot_price") * 2
])


selected_df = df_energy.filter(pl.col("is_active") == True 
& (pl.col("price_eur_per_mwh") < 50.0))





df = pl.DataFrame({
    "power_mw": [2.0, 3.5],
    "price_eur": [50.0, 60.0]
})

df = df.with_columns([
    (pl.col("power_mw") * pl.col("price_eur")).alias("revenue_eur")
])





df_telemetry = pl.DataFrame({
    "turbine_id": ["T1", "T2", "T3"],
    "power_mw": [2.5, 0.0, 4.0],
    "price_per_mwh": [50.0, 60.0, 45.0]
})



df = df_telemetry.with_columns(
    (((pl.col("power_mw") > 0)).alias("is_producing"))
)


df = df_telemetry.with_columns(
        ((pl.col("power_mw") > 0).alias("is_producing")),
        ((pl.col("power_mw")) * (pl.col("price_per_mwh"))).alias("hourly_revenue") )



df_telemetry = pl.DataFrame({
    "turbine_id": ["T1", "T2", "T3"],
    "power_mw": [2.5, 0.0, 4.0],
    "price_per_mwh": [50.0, 60.0, 0.0]
})


df = df_telemetry.with_columns([
    pl.when(pl.col("price_per_mwh") <= 0)
    .then(pl.lit("Curtail"))
    .otherwise(pl.lit("Produce"))
    .alias("market_action")
])




df_telemetry = pl.DataFrame({
    "turbine_id": ["T1", "T2", "T3"],
    "power_mw": [2.5, 0.0, 4.0],
    "price_per_mwh": [50.0, 60.0, 0.0]
})


df = df_telemetry.with_columns([
    pl.when(pl.col("power_mw") >= 3.0)
    .then(pl.lit("High"))
    .when(pl.col("power_mw") > 0)
    .then(pl.lit("Medium"))
    .otherwise(pl.lit("Stopped"))
    .alias("efficiency_tier")
]) 




df_data = pl.DataFrame({
    "site": ["Wind_North", "Wind_North", "Solar_South", "Solar_South", "Solar_South"],
    "power_mw": [2.0, 3.0, 1.5, 0.5, 0.5]
})

summary = df_data.group_by("site").agg([
    pl.col("power_mw").sum().alias("total_power"),
    pl.col("power_mw").mean().alias("avg_power"),
    pl.len().alias("record_count")
])





df_fleet = pl.DataFrame({
    "farm": ["North_Wind", "North_Wind", "South_Solar", "South_Solar", "North_Wind"],
    "power_mw": [2.5, 3.0, 1.0, 1.5, 2.0],
    "revenue_eur": [125.0, 150.0, 60.0, 90.0, 100.0]
})

summary = df_fleet.group_by("farm").agg([
    pl.col("revenue_eur").sum().alias("total_revenue"),
    (pl.col("power_mw").max()).alias("max_power"),
    pl.len().alias("readings_count"),
    pl.when(pl.col("power_mw") == 2.0)
  .then(pl.col("revenue_eur"))
  .otherwise(0.0)
  .sum()
  .alias("revenue_at_2mw") 
    
])





csv = pl.read_csv("data/db_hexoskin_connected.csv")

#print(csv[0])
#print(csv[0,3])
#print(csv[0, "source_name"])
#print(csv.head(5))

#print(csv.select(["AtHomePatientId", "timestamp"]).head(5))



r = csv.with_columns([
    pl.col("timestamp").str.to_datetime(time_zone="UTC")
])

#print(r.select(["AtHomePatientId", "timestamp"]).head(5))




r = csv.with_columns([
    pl.col("timestamp").str.to_datetime(time_zone="UTC"),
    (pl.col("cpap_use_simulated") - pl.col("cpap_use_baseline")).alias("cpap_diff")
])

#print(r.select(["cpap_use_simulated", "cpap_use_baseline", "cpap_diff"]).head(5))




r = csv.with_columns([
    pl.col("timestamp").str.to_datetime(time_zone="UTC"),
    (pl.col("cpap_use_simulated") - pl.col("cpap_use_baseline")).alias("cpap_diff")
]).filter(pl.col("cpap_diff") > 0)

#print(r.select(["cpap_use_simulated", "cpap_use_baseline", "cpap_diff"]).head(5))








df_prices = pl.DataFrame({
    "timestamp": ["2026-09-01 10:00:00", "2026-09-01 11:00:00"],
    "price_eur_mwh": [50.0, 75.0]
}).with_columns(pl.col("timestamp").str.to_datetime(time_zone="UTC"))

print(df_prices)


df_scada = pl.DataFrame({
    "timestamp": ["2026-09-01 09:14:22", "2026-09-01 10:48:05", "2026-09-01 11:05:10", "2026-09-01 10:59:59", "2026-09-01 12:05:10"],
    "power_mw": [2.1, 2.4, 3.0, 2.4, 3.0]
}).with_columns(pl.col("timestamp").str.to_datetime(time_zone="UTC"))

print(df_scada)



df_merged = df_scada.sort("timestamp").join_asof(
    df_prices,
    on="timestamp",
    strategy="backward"
).with_columns(
    (pl.col("power_mw") * pl.col("price_eur_mwh")).alias("instant_revenue")
)

print(df_merged)


df_local = df_merged.with_columns([
    pl.col("timestamp").dt.convert_time_zone("Europe/Paris").alias("local_time")
])
print(df_local.select(["timestamp", "local_time" , "instant_revenue"]).head(3))
