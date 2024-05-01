```
                                        Inverse Problem Python library
```
```
         __        ______  _______   _______   __      __  __  __  __     ______       _____  
        /  |      /      |/       \ /       \ /  \    /  |/  |/  |/  |    \    \      /    /     
        $$ |____  $$$$$$/ $$$$$$$  |$$$$$$$  |$$  \  /$$/ $$ |$$/ $$ |____ \ $$ \    / $$ /   
        $$      \   $$ |  $$ |__$$ |$$ |__$$ | $$  \/$$/  $$ |/  |$$      \ \ $$ \  / $$ /    
        $$$$$$$  |  $$ |  $$    $$/ $$    $$/   $$  $$/   $$ |$$ |$$$$$$$  | | $$$$$$$$ /     
        $$ |  $$ |  $$ |  $$$$$$$/  $$$$$$$/     $$$$/    $$ |$$ |$$ |  $$ | | $$$$$$$$ |     
        $$ |  $$ | _$$ |_ $$ |      $$ |          $$ |    $$ |$$ |$$ |__$$ |/ $$ /  \ $$ \    
        $$ |  $$ |/ $$   |$$ |      $$ |          $$ |    $$ |$$ |$$    $$/  $$ /    \ $$ \   
        $$/   $$/ $$$$$$/ $$/       $$/           $$/     $$/ $$/ $$$$$$$/_ $$_/      \_$$_\  

```
```
                                        https://hippylib.github.io
```

`hIPPYlibx` depends on [FEniCSx](https://fenicsproject.org/) version 0.8.0 released in April 2024.

`FEniCSx` needs to be built with the following dependencies enabled:
* `numpy`, `scipy`, `matplotlib`, `mpi4py`
* `petsc4py` (version 3.10.0 or above)
* `slepc4py` (version 3.10.0 or above)

# FEniCSx installation
## Run FEniCSx from Docker (Linux, MacOS, Windows)
`FEniCSx` can be run easily using their prebuilt `Docker` images.
First you will need to install [Docker](https://www.docker.com/) on your system. MacOS and Windows users should preferably use Docker for Mac or Docker for Windows --- if it is compatible with their system --- instead of the legacy version Docker Toolbox.