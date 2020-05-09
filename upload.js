/* Creates a pre-signed upload url and then stores a reference in a table */
exports.createUploadUrl = async params => {
 
    var { databaseHandler, bucketHandler } = params;
 
    // Create id for upload
    var uploadId = uuidv4();
 
    // Retrieve pre-signed url
    var bucketDataPromise = createPresignedPostPromise({
        Bucket: process.env.BUCKET_UPLOADS,
        Expires: 60 * 60,
        Conditions: [            
            ["content-length-range", 0, 300000], // 300kb
            [ "eq", "$key", uploadId],
            [ "eq", "$Content-Type", 'image/jpeg' ],
        ]
    });
 
    // var ddbData = await ddbDataPromise;
    var bucketData = await bucketDataPromise;
 
    // Wait for database handler to complete operation and then return
    return Helpers.generateResponse({
        data: {
            uploadData: bucketData,
            additionalFields: {
                key: uploadId,
                "Content-Type": 'image/jpeg',
            },
        },
        statusCode: 200
    });
}