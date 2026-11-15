#!/usr/bin/env python3
"""Download every public data set used in the study into <repo>/data_raw (≈1.4 GB).

Sources (all public; cite the original providers):
  * Open Soil Spectral Library v1.3 (OSSL) — https://storage.googleapis.com/soilspec4gg-public/datasets/
      ICRAF_ISRIC (VisNIR, MIR), KSSL (MIR, VisNIR), AFSIS1 (MIR), Neospectra (NIR).  CC-BY 4.0 / ODbL (AfSIS1).
  * Mango DMC and NIR spectra (Anderson, Walsh, Subedi, Walsh) — Mendeley Data doi:10.17632/46htwnp833 (CC BY 4.0)
  * Eigenvector Research data archive — SWRI diesel NIR, IDRC 2002 shoot-out tablets, CGL mixtures
  * Tecator — OpenML data id 505 (StatLib)
Usage:  python scripts/download_data.py [--dest ../../data_raw]
"""
import argparse
import hashlib
import os
import urllib.request
import zipfile

OSSL = "https://storage.googleapis.com/soilspec4gg-public/datasets"
FILES = []
for lib, stype in [("ICRAF_ISRIC", "visnir"), ("ICRAF_ISRIC", "mir"), ("KSSL", "mir"), ("KSSL", "visnir"),
                   ("AFSIS1", "mir"), ("Neospectra", "nir")]:
    for f in ("ossl_soillab_v1.3.csv.gz", "ossl_soilsite_v1.3.csv.gz", f"ossl_{stype}_v1.3.csv.gz"):
        FILES.append((f"{OSSL}/{lib}/{f}", f"ossl/{lib}/{f}"))
FILES += [
    ("https://data.mendeley.com/public-files/datasets/46htwnp833/files/10975117-717b-4504-a372-7845b4c42237/file_downloaded",
     "mango/MangoDMC_NIR_Data_v3.csv"),
    ("https://eigenvector.com/wp-content/uploads/2019/06/SWRI_Diesel_NIR_CSV.zip", "eigenvector/SWRI_Diesel_NIR_CSV.zip"),
    ("https://eigenvector.com/wp-content/uploads/2019/06/nir_shootout_2002.mat_.zip", "eigenvector/nir_shootout_2002.mat_.zip"),
    ("https://eigenvector.com/wp-content/uploads/2021/04/CGL_nir.mat_.zip", "eigenvector/CGL_nir.mat_.zip"),
    ("https://openml.org/data/v1/download/52617/tecator.arff", "tecator/tecator.arff"),
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", default=os.path.join(os.path.dirname(__file__), "..", "..", "..", "data_raw"))
    a = ap.parse_args()
    dest = os.path.abspath(a.dest)
    manifest = []
    for url, rel in FILES:
        out = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        if not os.path.exists(out) or os.path.getsize(out) == 0:
            print("downloading", url)
            req = urllib.request.Request(url, headers={"User-Agent": "research-script/1.0"})
            with urllib.request.urlopen(req, timeout=3600) as r, open(out, "wb") as f:
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    f.write(b)
        manifest.append(f"{sha256(out)}  {rel}")
    for z in ("nir_shootout_2002.mat_.zip", "CGL_nir.mat_.zip"):
        zp = os.path.join(dest, "eigenvector", z)
        with zipfile.ZipFile(zp) as zz:
            zz.extractall(os.path.join(dest, "eigenvector", z.replace(".zip", "_x")))
    open(os.path.join(dest, "SHA256SUMS.txt"), "w").write("\n".join(manifest) + "\n")
    print("done; checksums written to", os.path.join(dest, "SHA256SUMS.txt"))


if __name__ == "__main__":
    main()
