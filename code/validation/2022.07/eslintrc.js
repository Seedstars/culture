module.exports = {
    extends: ['airbnb-typescript', 'prettier', 'plugin:prettier/recommended'],
    rules: {
        'react/jsx-indent': ['error', 4],
        'react/jsx-indent-props': ['error', 4],
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
    },
    parserOptions: {
        project: './tsconfig.json',
    },
};