<?php
	# $env_var = getenv('OPENSHIFT_ENV_VAR');

	# $ip = getenv("REMOTE_ADDR"); // obtém o número ip do usuário
	$mysql = getenv("MYSQL_SERVICE_HOST");
	echo 'My sql service host is ' .$mysql;
?>