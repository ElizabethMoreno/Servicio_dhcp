# -*- coding: utf-8 -*-

import sys
import commands
import re

comprobacion = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

if sys.argv[1] == "-l":
	concecion_dhcp = commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep lease.*.{ |sort |uniq")
	concecion_dhcp = concecion_dhcp.replace("lease", "");
	concecion_dhcp = concecion_dhcp.replace("{", "");
	reserva_dhcp = commands.getoutput("cat /etc/dhcp/dhcpd.conf |grep host -A2|grep 'fixed-address' |sort |uniq")
	reserva_dhcp = reserva_dhcp.replace("fixed-address", "");
	reserva_dhcp = reserva_dhcp.replace(";", "");
	print "IPs Concedidas:"
	print concecion_dhcp
	if len(reserva_dhcp) == 0:
		print "No hay IPs reservadas"
	else:
		print "IPs Reservadas:"
		print reserva_dhcp
elif comprobacion.match(sys.argv[1]):
	concecion_dhcp = commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep -A6 '%s' |grep 'hardware ethernet' | sort |uniq" % sys.argv[1])
	concecion_dhcp = concecion_dhcp.replace("hardware ethernet", "");
	concecion_dhcp = concecion_dhcp.replace(";", "");
	if len(concecion_dhcp) == 0:
		print "La IP introducida no ha sido concedida."
	else:
		print "La MAC de la ip concedida es: ", concecion_dhcp
else:
	print "El argumento no coincide con una IP."