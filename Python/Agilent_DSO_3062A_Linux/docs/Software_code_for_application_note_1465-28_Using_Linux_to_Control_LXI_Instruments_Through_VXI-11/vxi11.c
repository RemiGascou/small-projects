// vxi11.c
// VXI-11 example program
// Copyright (C) 2007 Agilent Technologies
//
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License
// as published by the Free Software Foundation; either version 2
// of the License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// The GNU General Public License is available at
// http://www.gnu.org/copyleft/gpl.html.

#include "vxi11_xdr.c"
#include "vxi11_clnt.c"

#define VXI11_IP_ADDRESS			"134.40.175.150"
#define VXI11_LOGICAL_DEVICE		"inst0"
#define VXI11_BUFFER_SIZE			1024
#define VXI11_TIMEOUT_MS			10000

char Buffer[VXI11_BUFFER_SIZE]; // Buffer for instrument I/O

void send_string(CLIENT *VXI11Link,Device_Link lid,char string[])
{
	Device_WriteParms MyDevice_WriteParms; // Function parameters
	Device_WriteResp *MyDevice_WriteResp; // Return parameters
	
	MyDevice_WriteParms.lid = lid; // VXI-11 link ID
	MyDevice_WriteParms.io_timeout = VXI11_TIMEOUT_MS; // Timeout in ms
	MyDevice_WriteParms.lock_timeout = VXI11_TIMEOUT_MS; // Timeout in ms
	MyDevice_WriteParms.flags = 0; // Not used here, see VXI-11 specification
	MyDevice_WriteParms.data.data_val = string; // Data to send
	MyDevice_WriteParms.data.data_len = strlen(string); // Number of characters
	if((MyDevice_WriteResp=device_write_1(&MyDevice_WriteParms,VXI11Link))==
		NULL) {
		printf("Error: VXI-11 device_write returned NULL pointer.\n");
		clnt_perror(VXI11Link,"send_string"); // Print RPC error to stderr
		exit(1);
	}
	
	return;
}

void read_string(CLIENT *VXI11Link,Device_Link lid,char *buffer)
{
	Device_ReadParms MyDevice_ReadParms; // Function parameters
	Device_ReadResp *MyDevice_ReadResp; // Return parameters
	
	MyDevice_ReadParms.lid = lid; // VXI-11 link ID
	MyDevice_ReadParms.requestSize = VXI11_BUFFER_SIZE; // Maximum characters
	MyDevice_ReadParms.io_timeout = VXI11_TIMEOUT_MS; // Timeout in ms
	MyDevice_ReadParms.lock_timeout = VXI11_TIMEOUT_MS; // Timeout in ms
	MyDevice_ReadParms.flags = 0; // Not used here, see VXI-11 specification
	MyDevice_ReadParms.termChar = '\n'; // Read termination character
	if((MyDevice_ReadResp=device_read_1(&MyDevice_ReadParms,VXI11Link))==
		NULL) {
		printf("Error: VXI-11 function device_read returned NULL pointer.\n");
		clnt_perror(VXI11Link,"read_string"); // Print RPC error to stderr
		exit(1);
	}
	strncpy(buffer,MyDevice_ReadResp->data.data_val,
		MyDevice_ReadResp->data.data_len); // Copy to target buffer
	buffer[MyDevice_ReadResp->data.data_len]=0; // Add zero character (EOS)
	
	return;
}

void vxi11_trigger(CLIENT *VXI11Link,Device_Link lid)
{
	Device_GenericParms MyDevice_GenericParms;
	
	MyDevice_GenericParms.lid = lid; // VXI-11 link ID
	MyDevice_GenericParms.flags = 0; // Not used here, see VXI-11 specification
	MyDevice_GenericParms.io_timeout = VXI11_TIMEOUT_MS; // Timeout in ms
	MyDevice_GenericParms.lock_timeout = VXI11_TIMEOUT_MS; // Timeout in ms
	if(device_trigger_1(&MyDevice_GenericParms,VXI11Link)==NULL) {
		printf("Error: VXI-11 device_trigger returned NULL pointer.\n");
		clnt_perror(VXI11Link,"vxi11_trigger"); // Print RPC error to stderr
		exit(1);
	}
	
	return;
}

void vxi11_clear(CLIENT *VXI11Link,Device_Link lid)
{
	Device_GenericParms MyDevice_GenericParms;
	
	MyDevice_GenericParms.lid = lid; // VXI-11 link ID
	MyDevice_GenericParms.flags = 0; // Not used here, see VXI-11 specification
	MyDevice_GenericParms.io_timeout = VXI11_TIMEOUT_MS; // Timeout in ms
	MyDevice_GenericParms.lock_timeout = VXI11_TIMEOUT_MS; // Timeout in ms
	if(device_clear_1(&MyDevice_GenericParms,VXI11Link)==NULL) {
		printf("Error: VXI-11 device_clear returned NULL pointer.\n");
		clnt_perror(VXI11Link,"vxi11_clear"); // Print RPC error to stderr
		exit(1);
	}
	
	return;
}

unsigned char vxi11_readstb(CLIENT *VXI11Link,Device_Link lid)
{
	Device_GenericParms MyDevice_GenericParms;
	Device_ReadStbResp *MyDevice_ReadStbResp;
	
	MyDevice_GenericParms.lid = lid; // VXI-11 link ID
	MyDevice_GenericParms.flags = 0; // Not used here, see VXI-11 specification
	MyDevice_GenericParms.io_timeout = VXI11_TIMEOUT_MS; // Timeout in ms
	MyDevice_GenericParms.lock_timeout = VXI11_TIMEOUT_MS; // Timeout in ms
	if((MyDevice_ReadStbResp=device_readstb_1(&MyDevice_GenericParms,VXI11Link))
		==NULL) {
		printf("Error: VXI-11 device_readstb returned NULL pointer.\n");
		clnt_perror(VXI11Link,"vxi11_clear"); // Print RPC error to stderr
		exit(1);
	}
	
	return MyDevice_ReadStbResp->stb;
}

int main()
{
	CLIENT *VXI11Link; // Handle to RPC connection (core channel)
	Device_Link DeviceLink; // Handle to VXI-11 link to logical device
	unsigned short AbortSocket; // Port to use for abort channel
	pid_t process;
		
	// Initialize connection to the VXI-11 RPC server
	VXI11Link = clnt_create(VXI11_IP_ADDRESS, // Defined above
		DEVICE_CORE, // Defined in vxi11.h
		DEVICE_CORE_VERSION, // Defined in vxi11.h
		"tcp"); // Transport protocol (tcp or udp)
	if(VXI11Link==0) {
		printf("Error: clnt_create() returned NULL pointer.\n");
		clnt_pcreateerror("main"); // Print RPC error to stderr
		exit(1);
	}

	// Initialize VXI-11 link to logical device
	Create_LinkParms MyCreate_LinkParms; // Function parameters
	Create_LinkResp *MyCreate_LinkResp; // Return parameters
	MyCreate_LinkParms.clientId = 0; // Not used
	MyCreate_LinkParms.lockDevice = 0; // Do not try to lock device
	MyCreate_LinkParms.lock_timeout = VXI11_TIMEOUT_MS; // Not used
	MyCreate_LinkParms.device = VXI11_LOGICAL_DEVICE; // See above
	if((MyCreate_LinkResp=create_link_1(&MyCreate_LinkParms,VXI11Link))
		==NULL) {
		printf("Error: VXI-11 function create_link returned NULL pointer.\n");
		clnt_perror(VXI11Link,"main"); // Print RPC error to stderr
		exit(1);
	}
	printf("Abort port number is %u\n",MyCreate_LinkResp->abortPort);
	printf("Maximum send message size is %u\n",MyCreate_LinkResp->maxRecvSize);

	// Store VXI-11 link ID etc. for subsequent VXI-11 calls
 	DeviceLink = MyCreate_LinkResp->lid;
	AbortSocket = MyCreate_LinkResp->abortPort;

	// Read instrument's ID string
	send_string(VXI11Link,DeviceLink,"*IDN?\n");
	read_string(VXI11Link,DeviceLink,Buffer);
	printf("Instrument ID: %s\n",Buffer);
	
	// Read instrument's status byte
	printf("Status byte: %u\n",vxi11_readstb(VXI11Link,DeviceLink));
		
	// Close VXI-11 link using VXI-11 destroy_link function
	if(destroy_link_1(&DeviceLink,VXI11Link)==NULL)
	{
		printf("Error: VXI-11 function destroy_link returned NULL pointer...\n");
		clnt_perror(VXI11Link,"main"); // Print RPC error to stderr
		exit(1);
	}

	// Close connection to RPC server
	clnt_destroy(VXI11Link);

	exit(0);
}
