# LWH Draw

Logistics Warehouse's own copy of the free **draw.io** diagram editor, for warehouse floor plans, rack and bay layouts, dock assignments, and process flowcharts.

**Live at:** https://draw.logisticswarehouse.net

## What's different from stock draw.io
- **LWH Warehouse Layout** shape library in the left sidebar: pallets, floor bays, rack bays and runs, aisles, dock doors, 53' trailer, forklift, columns, walls, offices, staging, notes. Drawn to scale at **10 px = 1 ft**, so a layout drawn with them is to scale.
- LWH colors in the color picker (red, dark red, black, grays, plus status green/amber).
- Cloud logins (Google Drive, OneDrive, Dropbox, GitHub) are turned off since this is self-hosted. Save diagrams to your computer (**Device**). Saving into your Google Drive desktop folder keeps them in Drive.
- LWH name and icons.

Everything runs in the browser; diagrams are not uploaded anywhere.

## Changing settings
- Colors, default libraries and the warehouse shapes: `js/PreConfig.js` (`window.DRAWIO_CONFIG`).
- After changing any file, run `python3 update-sw-revisions.py` so installed copies refresh.

## Hosting
GitHub Pages from the `main` branch (root). `CNAME` = `draw.logisticswarehouse.net`; DNS: CNAME `draw` → `nbr1hawgfan.github.io` (Squarespace → DNS Settings → Custom records).

## License
draw.io is © JGraph Ltd / draw.io AG, licensed under the Apache License 2.0 (see `LICENSE`). This is draw.io version 32.6.1 with LWH configuration changes.
