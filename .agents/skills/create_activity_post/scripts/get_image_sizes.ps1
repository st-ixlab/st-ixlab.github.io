param (
    [Parameter(Mandatory=$true)]
    [string]$DirectoryPath
)

Add-Type -AssemblyName System.Drawing
Get-ChildItem -Path $DirectoryPath -Filter *.* -Include *.jpg,*.jpeg,*.png | ForEach-Object {
    try {
        $img = [System.Drawing.Image]::FromFile($_.FullName)
        $w = $img.Width
        $h = $img.Height
        $orientation = 1
        if ($img.PropertyIdList -contains 274) {
            $prop = $img.GetPropertyItem(274)
            $orientation = [BitConverter]::ToInt16($prop.Value, 0)
        }
        # EXIF orientation 5-8 means the image is rotated 90 or 270 degrees
        if ($orientation -ge 5 -and $orientation -le 8) {
            $w = $img.Height
            $h = $img.Width
        }
        Write-Output "$($_.Name) $w $h"
        $img.Dispose()
    } catch {
        Write-Warning "Failed to process $($_.Name): $_"
    }
}
