Feature: Interact with Windows Media Player

  @play @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Play button functionality in media player
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "AVI_Sample_File"
    Then I click on the play button
    Then I wait for 5 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @pause @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Pause functionality in media player
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "AVI_Sample_File"
    Then I click on the play button
    Then I wait for 2 seconds
    Then I "pause" the media playback
    Then I wait for 2 seconds
    Then I "play" the media playback
    Then I wait for 2 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @avi @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media Player plays .avi file format
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "AVI_Sample_File"
    Then I click on the play button
    Then I wait for 5 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @wmv @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media Player plays .wmv file format
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "WMV_Sample_File"
    Then I click on the play button
    Then I wait for 5 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @mpg @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media Player plays .mpg file format
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "MPG_Sample_File"
    Then I click on the play button
    Then I wait for 5 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @mpeg @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media Player plays .mpeg file format
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "MPEG_Sample_File"
    Then I click on the play button
    Then I wait for 5 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @mov @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media Player plays .mov file format
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "MOV_Sample_File"
    Then I click on the play button
    Then I wait for 5 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @mp3 @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media Player plays .mp3 file format
    Given the Windows Media Player application is started
    When I click on the "Music" tree item
    Then I click on the "MP3_Sample_Files" list item
    Then I click on the play button
    Then I wait for 5 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @wma @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media Player plays .wma file format
    Given the Windows Media Player application is started
    When I click on the "Music" tree item
    Then I click on the "WMA_Sample_Files" list item
    Then I click on the play button
    Then I wait for 5 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @wav @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media Player plays .wav file format
    Given the Windows Media Player application is started
    When I click on the "Music" tree item
    Then I click on the "WAV_Sample_File" list item
    Then I click on the play button
    Then I wait for 5 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @mid @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media Player plays .mid file format
    Given the Windows Media Player application is started
    When I click on the "Other media" tree item
    Then I click on the "MID_Sample_File"
    Then I click on the play button
    Then I wait for 8 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @au @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media Player plays .au file format
    Given the Windows Media Player application is started
    When I click on the "Other media" tree item
    Then I click on the "AU_Sample_File"
    Then I click on the play button
    Then I wait for 8 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @pause_Shortcut @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Shortcut key for pause
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "AVI_Sample_File"
    Then I click on the play button
    Then I wait for 2 seconds
    Then the application should be interacted with successfully
    Then I "pause" the media playback
    Then I wait for 2 seconds
    Then the application should be closed

  @midi @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media Player plays .midi file format
    Given the Windows Media Player application is started
    When I click on the "Music" tree item
    Then I click on the "Ringtone 1" list item
    Then I click on the play button
    Then I wait for 5 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @mute @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Mute button functionality in media player
    Given the Windows Media Player application is started
    When I click on the "Music" tree item
    Then I click on the "Ringtone 1" list item
    Then I click on the play button
    Then I wait for 2 seconds
    Then I click on the mute button
    Then I wait for 2 seconds
    Then I click on the mute button
    Then I wait for 2 seconds
    Then the application should be interacted with successfully
    Then the application should be closed
