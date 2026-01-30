|  | GEOS-access | ACCESS-OM3 | Note |
| --- | ------------ | ------------ | ---- |
| ALLOW_GLC_RUNOFF_DIAGNOSTICS | * | False | N/A |
| APPROX_NET_MASS_SRC | False | * | default=.false. |
| BODNER_DETECT_MLD | * | False | N/A |
| BOUNDARY_EXTRAPOLATION | False | * | GEOS Regridding specific  |
| BT_LINEAR_FREQ_DRAG | * | False | N/A |
| DEPRESS_INITIAL_SURFACE | * | False | initialization related  |
| DIRECT_EPBL_MIXING_CALC | * | False | N/A |
| DO_SKEB | * | False | N/A |
| ENTHALPY_FROM_COUPLER | * | True |  in NUOPC |
| EPBL_BBL_EFFIC | * | 0.0 | N/A |
| EPBL_BBL_TIDAL_EFFIC | * | 0.0 | N/A |
| EPBL_EQD_DIFFUSIVITY_SHAPE | * | False | N/A |
| EPBL_EQD_DIFFUSIVITY_VELOCITY | * | False |  N/A |
| EPBL_EQD_DIFFUSIVITY_VELOCITY_H | * | False | N/A |
| EPBL_MLD_ITER_BUG | * | True | N/A |
| EPBL_OPTIONS_DIFF | * | 0  |  N/A |
| EPS_OMESH | * | 1.0E-13 | in NUOPC |
| GEOM_FILE | * | access-om3.mom6.geometry.nc |  in NUOPC |
| HOR_REGRID_ANSWER_DATE | * | 99991231 | initialization related |
| HYCOM1_ONLY_IMPROVES | False | * | GEOS Regridding specific |
| ICE_SALT_CONCENTRATION | 0.0 | 0.005 | GEOS specific |
| INTERPOLATION_SCHEME | P1M_H2 | * | GEOS Regridding specific |
| INTWAVE_REMAPPING_USE_OM4_SUBCELLS | True | False |  |
| LATENT_HEAT_VAPORIZATION | 2.4665E+06 | 2.501E+06 |  GEOS Specific|
| LIGHTEST_DENSITY | * | 1035.0 | initialization related |
| MASKING_DEPTH | 0.0 | -9999.0 | GEOS specific |
| MASS_WEIGHT_IN_PGF_VANISHED_ONLY | * | False | N/A |
| MAXIMUM_DEPTH | 6500.0 | 6000.0 | GEOS specific |
| MAXIMUM_INT_DEPTH_CONFIG | FNC1:5,8000.0,1.0,.01 | * |  GEOS specific |
| MAX_LAYER_THICKNESS_CONFIG | FNC1:400,31000.0,0.1,.01 | * | GEOS specific  |
| MEKE_POSITIVE | * | False | N/A |
| MINIMUM_DEPTH | 9.5 | 0.0 | GEOS specific |
| MLD_EN_VALS | 3*0.0 | 25.0, 2500.0, 2.5E+05 | **reset in the code** |
| OCEAN_SURFACE_STAGGER | "C" | "A" | GEOS specific |
| OPACITY_BAND_WAVELENGTHS | * | 0.0, 550.0, 700.0, 2800.0 | N/A |
| OPACITY_VALUES_MANIZZA | * | 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0 | N/A |
| REGRIDDING_COORDINATE_MODE | HYCOM1 | ZSTAR | GEOS specific |
| REGRID_ACCELERATE_INIT | * | False |  |
| REGRID_COMPRESSIBILITY_FRACTION | 0.0 | * |  |
| REMAP_UV_USING_OLD_ALG | True | False | GEOS specific |
| REMAP_VEL_CONSERVE_KE | * | False |  |
| RESET_INTXPA_INTEGRAL_FLATTEST | * | False | N/A |
| RESTORE_FLUX_RHO | 1035.0 | * | FMS specific |
| RHO_PGF_REF_BUG | * | True | N/A |
| SET_DTBT_USE_BT_CONT | * | False | N/A |
| SQG_EXPO | 1.0 | * | lateral_mixing_coeffs, default=1.0 |
| STREAMING_FILTER_K1 | False | * | tides, default=.false.|
| STREAMING_FILTER_M2 | False | * | tides, default=.false.|
| SURFACE_FORCING_ANSWER_DATE | 99991231 | * | FMS specific |
| TFREEZE_S_IS_PRACS | * | False | N/A |
| TFREEZE_T_IS_POTT | * | False | N/A |
| THERMO_SPANS_COUPLING | False | True | GEOS specific |
| TIDEAMP_FILE | tidal_amplitude.v20140616.nc | tideamp.nc |  |
| TKE_TIDAL_RHO | 1035.0 | * | FMS specific, default |
| TOPO_FILE | ocean_topog.nc | topog.nc |  |
| TRADV_SPANS_COUPLING | * | True | N/A |
| USE_CALVING_HEAT_CONTENT | False | True | no calving |
| USE_CONTEMP_ABSSAL | False | True | not compatible with restarts |
| USE_FILTER | * | False | N/A |
| USE_RIGID_SEA_ICE | False | True | no ice regidity |
| USE_RIVER_HEAT_CONTENT | False | True | no heat content |
| VERTEX_SHEAR_GEOMETRIC_MEAN | * | False | N/A |
| VERTEX_SHEAR_THICKNESS_MEAN | * | False | N/A |
| VERTEX_SHEAR_VISCOSITY_BUG | * | True | N/A |
