<?php
function GetInformationProfile(){
	global $Nick;
	global $userId;
	global $mysqli;
	global $balance;
	global $UserInfo;
	$message = $Nick.', ваш профиль:'."<br>".
	'🔎ID: '.$UserInfo['id']."<br>".
	'👔Ник: '.$Nick."<br>".
	'💰Баланс:  '.($balance)."$";
	
	return $message;
	
}

function Stakan($stavka,$summ){
	global $balance;
	global $Nick;
	$Rand = rand(1,3);
	if($summ>0){
		if($stavka>0 && $stavka<=3){
			if($balance >= $summ){
				if ($Rand == $stavka){
					SetFieldF('balance',$balance+floor($summ*2));
					$message = $Nick.', вы угадали ваш приз: '.($summ*2)."$<br>"."💰Баланс: ".($balance+floor($summ*2))."$";
				}else{
					SetFieldF('balance',$balance-floor($summ));
					$message = $Nick.', вы не угадали это был '.$Rand."-й напёрсток <br>"."💰Баланс: ".($balance-floor($summ*1))."$";
				}
			}else{
				$message = $Nick.', недостаточно денег.';
			}
		}
	}
	return $message;
	
}
function SetFieldF($field,$value){
	global $mysqli;
	global $userId;
	$mysqli->query("UPDATE `users` SET `".$field."` = '".$value."' WHERE `users`.`id_VK` = ".$userId.";");
}
function selectFromIDVK($result_set,$id){
	$k = 0;
	while(($row = $result_set->fetch_assoc()) !=false){
		if ($row['id_VK'] == $id){
			$k = 1;
			return $row;
		}
	}
	if ($k!=1){return false;}
}
?>