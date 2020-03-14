// Setup IO buffer for DEV_DEP_MSG_OUT message
usbtmc_buffer[0]=1; // DEV_DEP_MSG_OUT
usbtmc_buffer[1]=bTag; // Transfer ID (bTag)
usbtmc_buffer[2]=~(bTag); // Inverse of bTag
usbtmc_buffer[3]=0; // Reserved
usbtmc_buffer[4]=command_length&255; // Transfer size (first byte)
usbtmc_buffer[5]=(command_length>>8)&255; // Transfer size (second byte)
usbtmc_buffer[6]=(command_length>>16)&255; // Transfer size (third byte)
usbtmc_buffer[7]=(command_length>>24)&255; // Transfer size (fourth byte)
usbtmc_buffer[8]=1; // Message ends with this transfer
usbtmc_buffer[9]=0; // Reserved
usbtmc_buffer[10]=0; // Reserved
usbtmc_buffer[11]=0; // Reserved

// Append write buffer (instrument command) to USBTMC message
if(copy_from_user(&(usbtmc_buffer[12]),command_buffer,command_length)) {
    // There must have been an addressing problem
    return -EFAULT;
}

// Add zero bytes to achieve 4-byte alignment
n_bytes=12+command_length;
if(command_length % 4 == 0) {
    n_bytes+=4-command_length%4;
    for(n=12+command_length;n<n_bytes;n++) usbtmc_buffer[n]=0;
}
// Create pipe for bulk out transfer
pipe = usb_sndbulkpipe(usb_dev,bulk_out);

// Send bulk URB
retval = usb_bulk_msg(
    usb_dev,
    pipe,
    usbtmc_buffer,
    n_bytes,
    &actual,
    USBTMC_USB_TIMEOUT
);
