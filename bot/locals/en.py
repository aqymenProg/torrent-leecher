from bot.locals import Local

LOCAL = Local({
    'WRONG_ROOM' : 'I a\'m not suppose to be here.\nID : <code>{CHAT_ID}</code>',
    'WELCOME_MESSAGE' : "Hi!\nI'm <b>Leech Bot</b>!\nMy Owner is Aqymen\n>",
    'PASS_REQUIRED' : '\n\nUse <code>/{cmd_pass} </code>to enter the password.',
    'LEECH_LIST_MESSAGE_HEADER' : '<b>Leech Status</b>',
    'LEECH_LIST_FORMAT' : 'Name: <code>{name}</code>\nStatus: {status}\nID: <code>{gid}</code>\n\n',
    'ARIA2_CHECKING_LINK' : "🔎Checking Your Link....",
    'ARIA2_DOWNLOAD_STATUS' : " ➟ File Name :\n➟ <code>{name}</code>\n➟ File Size : {total_size}\n➟ Status : Downloading\n➟ Download Speed : {download_speed}\n➟ {block}\n➟ Downloaded : {percentage}\n➟ Seeders : {seeder}\n➟ ETA : {eta}\n➟ File ID : <code>{gid}",
    'ARIA2_DOWNLOAD_SUCCESS' : 'File downloaded\nFile Name: k<code>{name}</code>',
    'ARIA2_DOWNLOAD_CANCELED' : 'Download canceled\nFile Name : <code>{name}</code>',
    'ARIA2_DEAD_LINK' : '❗Download auto canceled\nFile Name : <code>{name}</code>\n❌Your Torrent/Link is Dead❌.',
    'ARIA2_NO_URI' : '❗Link is invalid.',
    'UPLOADING_FILE' : '➟ Status : Uploading\n➟ File Name : <code>{name}</code>',
    'UPLOADING_PROGRESS' : '➟ File Name :\n➟ <code>{name}</code>\n➟ File Size : {size}\n➟ Status : Uploading\n➟ Upload Speed : {upload_speed}ps\n➟ {block}\n➟ Uploaded : {percentage}%\n➟ ETA : {eta}',
    'UPLOAD_FAILED_FILE_MISSING' : '❗Upload Error\nFile Name : <code>{name}</code>',
    'GENERATE_THUMBNAIL' : '➟ Thumbnail Generating Wait.\n➟ <code>{name}</code>',
    'SPLIT_FILE' : '➟ Spliting :\n➟ <code>{name}</code>',
    'SPLIT_FAILED' : '❌Error Split : Failed.\n➟ <code>{name}</code>',
    'THUMBNAIL_NO_PHOTO' : 'Set <code>/{cmd_set_thumbnail}</code> as your photo caption.',
    'THUMBNAIL_DOWNLOADING' : '➟ Downloading thumbnail.',
    'THUMBNAIL_DOWNLOADED' : '➟ Thumbnail download.',
    'THUMBNAIL_APPLIED' : '➟ Thumbnail applied.',
    'THUMBNAIL_DELETING' : '➟ Deleting thumbnail.',
    'THUMBNAIL_RESET' : '➟ Thumbnail reset.',
    'UPLOAD_AS_DOC' : 'Upload as document set to {status}.',
    'UPLOAD_AS_ZIP' : 'Upload as zip file set to {status}.',
    'TRACKER_RESET' : 'Default torrent tracker reset.',
    'TRACKER_APPLIED' : 'Default torrent tracker applied.',
    'HELP_MESSAGE_HEADER' : '<b>Bot Command</b>',
    'NO_HELP_INFO' : 'no information',
    'COMMAND_START' : 'start bot',
    'COMMAND_PASSWORD' : 'enter password that required',
    'COMMAND_HELP' : 'this message',
    'COMMAND_LEECH' : 'leech link or magnet',
    'COMMAND_CANCEL_LEECH' : 'cancel leeching',
    'COMMAND_LEECH_LIST' : 'list on going leech',
    'COMMAND_SET_THUMBNAIL' : 'set custom video thumbail',
    'COMMAND_RESET_THUMBNAIL' : 'reset custom video thumbnail',
    'COMMAND_UPLOAD_AS_DOC' : 'toggle upload anything as document',
    'COMMAND_UPLOAD_AS_ZIP' : 'toggle upload anything as bundled zipfile',
    'COMMAND_SET_TRACKER' : 'set default tracker, sparated by newline',
    'BLOCK_EMPTY' : "□",
    "BLOCK_FILLED" : "■"
})
