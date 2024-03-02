module.exports = {
    extends: ['airbnb', 'airbnb-typescript', 'prettier', 'plugin:prettier/recommended'],
    rules: {
        'react/jsx-indent': ['error', 4],
        'react/jsx-indent-props': ['error', 4],
        'react/function-component-definition': [2, {namedComponents: 'arrow-function'}],
        'react/jsx-no-useless-fragment': [2, {allowExpressions: true}],
        'import/prefer-default-export': 0,
        'no-param-reassign': 0,
        'react/prop-types': 0,
        'react/require-default-props': 0,
        '@typescript-eslint/no-explicit-any': 2,
        'prefer-destructuring': [
            'error',
            {
                array: false,
                object: true,
            },
            {
                enforceForRenamedProperties: false,
            },
        ],
        'import/no-cycle': 0,
    },
    parserOptions: {
        project: './tsconfig.json',
    },
};
