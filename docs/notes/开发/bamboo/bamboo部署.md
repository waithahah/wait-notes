 created system service user
2024-05-21 08:11:56,874 INFO  [spring-startup]  c.a.s.i.s.g.m.a.DefaultMeshKeyManager CONTROL_PLANE: Generated new signing key: CA3NxhTaQ0ka/nkekWTR5OL22RVN52dM2mKM97QcT5k
2024-05-21 08:11:57,415 INFO  [spring-startup]  c.a.s.i.s.g.m.a.DefaultMeshKeyManager SIDECAR: Generated new signing key: j1NR1VQJXHYtVH1wsPEPZQR/2zL0DEpOCUSi5YVnpdc
2024-05-21 08:12:08,899 INFO  [spring-startup]  c.a.s.i.s.g.m.DefaultSidecarManager Sidecar started after 12466ms
2024-05-21 08:12:15,458 INFO  [spring-startup]  c.a.s.i.hook.DefaultHookService Hook callback socket listening on 127.0.0.1:35036
2024-05-21 08:12:20,199 WARN  [spring-startup]  c.a.s.i.s.SecretScanningWiring Invalid value for 'secretscanning.email.maxsecrets': secretscanning.email.maxsecrets is not a positive integer. Using default value of 100 instead.
2024-05-21 08:12:20,398 INFO  [spring-startup]  c.a.s.i.bootstrap.BootstrapOperation Application created
2024-05-21 08:12:20,482 INFO  [spring-startup]  c.a.s.i.bootstrap.BootstrapOperation Directory created



docker exec 1854c00b1c96 java -jar /opt/atlassian/atlassian-agent-jar-with-dependencies.jar \
    -p bamboo \
    -m qkos@qkos.cn \
    -n qkos@qkos.cn \
    -o qk \
    -s BLJH-HJ3S-CVOE-SLME
