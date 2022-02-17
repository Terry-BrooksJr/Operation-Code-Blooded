//Requirements: Provide an Error Level Notification - if FirstName.includes('&') is true.
///Description for UI: This V3 Non-Destructive Data Hook is designed to iterate thought the array of records and evaluate an express that if True is a string with the string literal '&' in the Value of the FirstName field. 

//Expected Behavior: The expected behavior is to show and Error Level Warning to the Data Owner. Does not manipulate values. 

// In the Future, If you have additional unwanted string literals that are

module.exports = async ({ recordBatch, session, logger }) => {
    recordBatch.records.forEach((record) => {
        if (firstName.includes('&')) { //
            row.addError('firstName', 'Invalid Character Found, remover the \'&\'');}
        }
    );
};

// Alternative Implementation

module.exports = async ({ recordBatch, session, logger }) => {
    recordBatch.records.forEach((record) => {
        if (record['firstName'].includes('&')) { //Roby - Am I accessng the firstName Key correctly - I also had just if (firstName)
            row.addError('firstName', 'Invalid Character Found, remover the \'&\'');
        }
    }
    );
}; 