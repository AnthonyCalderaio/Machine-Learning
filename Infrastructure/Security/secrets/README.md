

## Helpful URL
`https://tech.serhatteker.com/post/2022-12/encrypt-and-decrypt-files-with-ssh-part-4/`

## Install
`# MacOS: $ brew install age`

## Create Keypair
`age-keygen -o keyfilename`


## To Encrypt file
`age -o NEWFILENAME -r PUBLICKEY FILETOENCRYPT`

## To Decrypt
`age --decrypt -i FILEWHERESECRETISLOCATED ENCRYPTEDFILENAME > NEWUNENCRYPYEDFILENAME`
