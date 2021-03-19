def get_id(ingredient_str):
    '''Transforms string input to pre-processed ID'''
    ingredient_id = ingredients_clean[ingredients_clean['raw_ingr'] ==ingredient_str]
    ingredient_id.reset_index(inplace=True)
    return ingredient_id.loc[0,'id']

def get_name(ingredient_id):
    '''Transforms ID back to pre-processed string'''
    ingredient_name = ingredients_clean[ingredients_clean['id'] == ingredient_id]
    ingredient_name.reset_index(inplace=True)
    return ingredient_name.loc[0,'replaced']

def find_match(ingredient_id,num_matches):
    '''Returns list of ingredient IDs and count of occurances'''
    total = final_df[final_df[ingredient_id]==1].sum()
    ids = total.sort_values(ascending=False)
    return list(ids.head(num_matches).index)

def list_to_names(ingredient_id_list):
    '''Takes in list of ingredient IDs and returns list of names'''
    list_ = []
    for id in ingredient_id_list:
        list_.append(get_name(id))
    return list_

def output_func(input_ingredient,num_matches=10):
    '''Combines other functions into a workflow'''
    num_matches += 1
    result = get_id(input_ingredient)
    ids = find_match(result,num_matches)
    names = list_to_names(ids)
    names.pop(0)
    return names
