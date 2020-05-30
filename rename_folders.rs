use std::env;
use std::fs::{read_dir, rename};
use std::path::PathBuf;

fn main() -> std::io::Result<()> {
    let current_dir = env::current_dir()?;
    let dir_folders = read_dir(current_dir)?
        .map(|res| 
            res.map(|e| (e.file_name(), e.file_type().unwrap().is_dir()))
        )
        .filter(|result_tuple| result_tuple.is_ok() && result_tuple.as_ref().unwrap().1)
        .map(|ok| ok.unwrap())
        .collect::<Vec<_>>();
    for folder in dir_folders {
        let folder_string: String = folder.0.to_str().unwrap().to_string();
        rename(folder_string.clone(), remove_padding(folder_string.clone()));
        println!("{}", remove_padding(folder_string));
    }
    Ok(())
}

fn remove_padding(folder: String) -> String {
    folder.trim_start_matches('0').to_string()
}
