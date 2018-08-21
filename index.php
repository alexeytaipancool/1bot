<?php

require_once('functions.php');



if (!isset($_REQUEST)) {
    return;
}
$confirmationToken = '';// Строка подтверждения
$token = '';//Access token группы
$data = json_decode(file_get_contents('php://input'));

switch ($data->type) {
case 'confirmation':
	echo $confirmationToken;
break;
case 'group_join':
	$peer_id = $data->object->user_id;
	$message = "🔔Благодрарим за подписку на наше сообщество.";
	$request_params = array(
		'message' => $message,
		'peer_id' => $peer_id,
		'access_token' => $token,
		'v' => '5.80'
	);
	$get_params = http_build_query($request_params);
	file_get_contents('https://api.vk.com/method/messages.send?'.$get_params);
	echo ('ok');
break;
case 'message_new':

$body = $data->object->text;
$peer_id = $data->object->peer_id;
$bodyx = explode(' ',$body);
$bodyl = mb_strtolower($body,"UTF-8");
$bodyxl = explode(' ',mb_strtolower($body,"UTF-8"));
$userId = $data->object->from_id;
$Users_get = json_decode(file_get_contents("https://api.vk.com/method/users.get?user_ids=".$userId."&name_case=Nom&v=5.80&access_token=".$token),1);
$UserFirstName = $Users_get['response'][0]['first_name'];
$mysqli = new mysqli("localhost", "", "", ""); // подключение к бд host, username, password, name_db
$mysqli->set_charset('utf8mb4');
$Users = $mysqli->query("SELECT * FROM `users` ");
$UserInfo = selectFromIDVK($Users,$userId);
$Nick = $UserInfo['name'];
$balance = $UserInfo['balance'];


switch($bodyxl[0]){
	
	case 'помощь':
	case 'команды':
	case 'меню': 
	$message = 
	'
	📒Профиль
	✒Ник [вкл/выкл]
	🥛Напёрсток [1-3] [сумма]';
	break;
	case 'профиль':
	$message = GetInformationProfile();
	break;
	case 'ник':
	if ($bodyxl[1] == 'вкл'){
		SetFieldF('nicknf',1);
		$message = "[id".$userId."|".$UserInfo['name']."]".', ваш ник включен.';
	}elseif($bodyxl[1] == 'выкл'){
		SetFieldF('nicknf',0);
		$message = $UserInfo['name'].', ваш ник вылючен.';
	}elseif((iconv_strlen(substr($body,7))>20)){
		$message = 'Максимальная длина ника 20.<br>Длина вашего ника: '.iconv_strlen(substr($body,7));
	}elseif(!empty($bodyxl[1])){
		SetFieldF('name',substr($body,7));
		$message = "Теперь вы '".substr($body,7)."'";
	}
	break;
	case 'напёрсток':
	case 'наперсток':
	$OneThree = $bodyx[1]*1;
	$Summ = $bodyx[2];
	$message = Stakan($OneThree,$Summ);
	break;
}

if(!$UserInfo){
	$M = 165000;
	$mysqli->query("INSERT INTO `users` (`id_VK`,`name`,`balance`) 
	VALUES (".$userId.",'".$UserFirstName."',".$M.")");
	$message = $UserFirstName.', вы успешно зарегистрировались, чтобы узнать команды напишите "команды" || "меню".';
}
$mysqli->close();
$request_params = array(
		'message' => $message,
		'peer_id' => $peer_id,
		'access_token' => $token,
		'v' => '5.80'
	);
$get_params = http_build_query($request_params);
file_get_contents('https://api.vk.com/method/messages.send?'.$get_params);
echo ('ok');
break;


}

?>