# === Stage 63: Add relationships between records where useful ===
# Project: FestivalPlan
def link_records(db):
    for f in db["festival"]:
        vendors = [v["id"] for v in db["vendors"] if v["festival_id"] == f["id"]]
        f["vendor_ids"] = vendors
        for t in db["tickets"]:
            if t["festival_id"] == f["id"]:
                t["artist_ids"] = [a["id"] for a in db["artists"] if a["festival_id"] == f["id"]]
        for s in db["schedule"]:
            if s["festival_id"] == f["id"]:
                s["artist_ids"] = [a["id"] for a in db["artists"] if a["festival_id"] == f["id"]]
        for v in db["volunteers"]:
            if v["festival_id"] == f["id"]:
                v["shift_ids"] = [sh["id"] for sh in db["shifts"] if sh["festival_id"] == f["id"]]
