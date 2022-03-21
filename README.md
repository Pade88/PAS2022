# PAS
Proiect Arhitecturi Software

## Version names and update legend. 
- [1-9].x.x = Major update (new features added). 
- x.[1-9].x = Minor update (refactoring versions, no new features). 
- x.x.[1-99]= Bug fix update. 

## Initial Commit 15 03 2022

# Status
    Version 1.0.0 -> Functional
    Version 1.0.1 -> Fixed (1), related to (2)
    Version 1.0.2 -> Fixed (3), to be tested
    Version 1.0.3 -> Fixed (15), to be tested
    Version 1.0.4 -> Fixed (20)
    Version 2.0.0 -> Implemented (5) and (6) -> Functional 
# ToDo
Level 1: ASAP
Level 2: Mandatory
Level 3: Maybe

    f(1) Companies are not loaded into gfx -> OPA, level 1, fixed in 1.0.1
    o(2) Implement / redesign sanity_check() for Product / Supplier / Company -> CRA, level 1
    f(3) Replace getters / setters with @property -> OPA/CRA, level 2 -> WIP started in 1.0.2
    o(4) Comments / annotations -> CRA, level 2
    f(5) <<Delete>> product handler -> OPA, level 2
    f(6) GUI for <<Delete>> product handler -> OPA, level 2
    o(7) Increase log coverage -> CRA, level 1
    o(8) Method check (metaclass-like) -> OPA, level 2
    o(9) Dissambly info in logs -> OPA, level 3
    o(10) UI/UX redesign -> CRA, level 3
    o(11) .ini for gfx -> OPA, level 2
    o(12) Database instead of json? -> ?, level 3
    o(13) Better handling of products list -> ?, level 3
    o(14) Conda venv / Docker build -> ?, level 3
    f(15) GUI may crash on suppliers list when company is set -> OPA, level 1
    o(16) Constant app test / create a class for unit test ( extend logger maybe) -> CRA, level 1
    o(17) Product table view may crash when new products are inserted -> OPA, level 1
    o(18) If the user accesses the list product, will notice that a crash occurs
    o(19) Missing diacritics can be noticed on the Add button / Looking for a supplier menu / Adding a supplier menu
    f(20) Logs are not working on Windows operating system
    o(21) Main supplier / company combo box does not sync when a item is deleted