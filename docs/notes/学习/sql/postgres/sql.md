SELECT * FROM pg_locks WHERE relation = 'public.t_video_analyse_task'::regclass;
SELECT pg_terminate_backend(1192272) FROM pg_locks WHERE relation = 'public.t_video_analyse_task'::regclass;


SHOW max_connections;
SELECT count(*) FROM pg_stat_activity;
SELECT datname, usename, application_name, client_addr, state 
FROM pg_stat_activity;
SELECT application_name, count(*)
FROM pg_stat_activity
GROUP BY application_name
ORDER BY count(*) DESC;

